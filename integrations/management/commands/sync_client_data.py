from django.db import connections

class Command():
    help = 'Synchronizes dealership data from client database to default database'

    def handle(self, *args, **options):
        try:
            # Ensure both database connections are available
            with connections['client'].cursor() as client_cursor:
                with connections['default'].cursor() as default_cursor:
                    # First, create the dealership table in default database if it doesn't exist
                    default_cursor.execute("""
                        CREATE TABLE IF NOT EXISTS dealership (
                            id SERIAL PRIMARY KEY,
                            name VARCHAR(255) NOT NULL,
                            address VARCHAR(255) NOT NULL,
                            city VARCHAR(100) NOT NULL,
                            state VARCHAR(50) NOT NULL,
                            zip_code VARCHAR(10) NOT NULL,
                            phone VARCHAR(20) NOT NULL,
                            email VARCHAR(254) NOT NULL,
                            website VARCHAR(200),
                            tax_id VARCHAR(20) NOT NULL,
                            active BOOLEAN DEFAULT TRUE,
                            created_at TIMESTAMP NOT NULL,
                            updated_at TIMESTAMP NOT NULL
                        )
                    """)

                    # Get all dealerships from client database
                    client_cursor.execute('SELECT * FROM dealership')
                    dealerships = client_cursor.fetchall()

                    # Get column names
                    client_cursor.execute("SELECT column_name FROM information_schema.columns WHERE table_name = 'dealership' ORDER BY ordinal_position")
                    columns = [col[0] for col in client_cursor.fetchall()]
                    
                    # Clear existing data in default database
                    default_cursor.execute('TRUNCATE TABLE dealership RESTART IDENTITY')

                    # Insert dealerships into default database
                    for dealership in dealerships:
                        placeholders = ', '.join(['%s'] * len(columns))
                        insert_query = f"INSERT INTO dealership ({', '.join(columns)}) VALUES ({placeholders})"
                        default_cursor.execute(insert_query, dealership)

            self.stdout.write(
                self.style.SUCCESS(f'Successfully synchronized {len(dealerships)} dealerships')
            )

        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error synchronizing dealerships: {str(e)}')
            )
