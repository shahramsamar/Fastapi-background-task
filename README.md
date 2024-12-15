# FastAPI Background Task

This repository demonstrates how to use **FastAPI** to manage and execute background tasks. It provides a simple implementation for asynchronous task handling, ideal for scenarios such as sending emails, processing data, or performing scheduled operations.

## Features

- Integration of FastAPI's background task functionality.
- Lightweight and asynchronous task execution.
- Easy-to-understand example for integrating background processes in FastAPI applications.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/shahramsamar/Fastapi-background-task.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Fastapi-background-task
   ```

3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

6. Access the API documentation:
   - Interactive API docs: `http://127.0.0.1:8000/docs`
   - Alternative API docs: `http://127.0.0.1:8000/redoc`

## Example Code

### Background Task Example
```python
from fastapi import FastAPI, BackgroundTasks

app = FastAPI()

def write_log(message: str):
    with open("log.txt", mode="a") as log:
        log.write(message + "\n")

@app.post("/log/")
def log_message(message: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_log, message)
    return {"message": "Log request received."}
```

## Usage

- Start the application and test the background task by sending a POST request to `/log/` with a message.
- Check the `log.txt` file for the recorded messages.

Example request:
```bash
curl -X POST "http://127.0.0.1:8000/log/" -H "Content-Type: application/json" -d '{"message": "Hello, background task!"}'
```

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes with clear messages.
4. Push your branch and create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

- **Author**: Shahramsamar
- **Email**: [shahramsamar2010@gmail.com](mailto:shahramsamar2010@gmail.com)
- **GitHub**: [Shahramsamar](https://github.com/shahramsamar)
![Alt](https://repobeats.axiom.co/api/embed/eabe6508a91fa38b4ace0060919094363916f544.svg "Repobeats analytics image")
