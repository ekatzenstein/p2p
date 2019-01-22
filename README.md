# Pandas-to-Production

Hackweek project. Dataframes to React.

## Getting Started

1. Install prerequisites.

   - `docker` and `docker-compose` (installed as part of Docker for Mac)

1. Start the stack.

   ```bash
   docker-compose build
   docker-compose up -d
   ```

1. Navigate to: http://localhost/

## Minio

1. `brew install minio/stable/mc`

1. `mc config host add minio http://127.0.0.1:9001 minio minio123`

1. `mc ls minio`