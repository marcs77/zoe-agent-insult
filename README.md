# zoe-agent-insult
An agent for Zoe (GUL) that provides insults from Monkey Island.

### Installation
 - Clone this repository in the zoe directory.
 - Add this to docker-compose.yml
   ```yml
   zoe-agent-insult:
      build: ./zoe-agent-insult
      depends_on:
        - kafka
      volumes:
        - './zoe-agent-insult/src:/code/src'
      command: 'monitor /code python3 -u /code/src/agent.py'
      environment:
        KAFKA_SERVERS: kafka:9092
   ```
### Usage
 - The intent format for this agent is as follows:
 ```python
 {
    'intent': 'insult.get',
    'username': '<Insert username here>',
    'locale': 'es' 
 }
 ```
 - The available locales are 'en' and 'es'
 - For example, in zoe's shell we can type: 
 ```{'intent':'insult.get', 'username':'marcs77', 'locale': 'es'}```
 
 - For testing purposes, it is useful to create a helper function for
zoe shell. In src/agent.py inside zoe-agent-shell, we can add:
  ```python
    def insult(user, locale='es'):
        return {
            'intent': 'insult.get',
            'username': user,
            'locale': locale
        }
  ```
  - Then ```insult('user','en')``` can be used as a command for the shell.
