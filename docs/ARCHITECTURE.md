## System Flow
```mermaid
sequenceDiagram
    participant Camera
    participant Gesture Detection
    participant Flask Server
    participant Web Interface
    
    Camera->>Gesture Detection: Hand landmarks
    Gesture Detection->>Flask Server: POST /calculate
    Flask Server->>Web Interface: WebSocket update