Quick and dirty Python bindings to the open world OWS2 API

To regenerate from database tables:

- sqlacodegen 'postgresql://postgres:admin@localhost:5432/openworldserver' > db_schema.py
- python .\generate_api_models.py

This will be used for a fastapi server later on, and facilitate experimentation with microservices for the game server