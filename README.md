# the-big-repository-of-knowledge
A repository full of various tutorials and references for different development tools.

The goal here is to learn 1 new tool per week. 

## Timeline
- Week of June 19th - 25th, 2022: RabbitMQ

## Sections

### RabbitMQ

Notes are in `RabbitMQ/RabbitMQ.tex`

#### RabidsMQ

RabidsMQ is a RabbitMQ wrapper that I wrote to prevent the reusage of boilerplate code often needed in the setup of RabbitMQ clients. Additionally, it allows for the transmission of header packets containing metadata about packet data and more.

#### Tutorials
1. Hello, World!
    - The simplest thing that does something
2. Task Queue
    - Creating a task queue for task load balancing via messaging
    - Exploring queue and message acknowledgement and durability to ensure tasks are completed and handled correctly.
3. Publish/Subscribe
    - Sending messages to many consumers at once
    - Learning the value of exchanges and how queues interact with them
