# the-big-repository-of-knowledge
A repository full of various tutorials and references for different development tools.

The goal here is to learn 1 new tool per week. 

## Timeline
|   Topic   |    Start Date    |    End Date     |   Progress   |  Notes |
| --------- | ---------------- | --------------- | ------------ | ------ |
| GraphQL   | July 11th, 2022  | July 18th       |  In-Progress |        | 
| Influx DB | June 26th, 2022  | July 9th, 2022  |     Done     | Delayed by a week due to school |
| RabbitMQ  | June 19th, 2022  | June 25th, 2022 |     Done     |        |

## Sections

### GraphQL

Notes are in `GraphQL/GraphQL/tex`

### Influx DB

Notes are in `InfluxDB/InfluxDB.tex`

This was pretty short, mostly just setting up a database using Docker and then simple querying via reads and writes.

Might pick this up again at a later date if I feel like there's more I need to learn on this, but moving onto `GraphQL` for the time being to stay motivated and on track.

### RabbitMQ

LaTeX notes are in `RabbitMQ/RabbitMQ.tex`

PDF notes are in `RabbitMQ/RabbitMQNotes.pdf`

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
4. Routing
    - Sending messages to specific nodes via topics and routing keys
    - Filtering messages sent to specific nodes via routing keys.
5. Topics
    - Extend Routing tutorial to be able to create complex topics to allow filtering by many criteria.
