# Pandas-to-Production

Hackweek project. Dataframes to React.

## Getting Started

1. Install prerequisites.

   - `docker` and `docker-compose` (installed as part of Docker for Mac)

1. Start the stack.

   ```bash
   make
   ```

1. View the stack.

   | App         | URL                    |
   | ----------- | ---------------------- |
   | Frontend    | http://localhost/      |
   | Backend API | http://localhost/api/  |
   | Swagger UI  | http://localhost:8080/ |

## Minio

1. `brew install minio/stable/mc`

1. `mc config host add minio http://127.0.0.1:9001 minio minio123`

1. `mc ls minio`
