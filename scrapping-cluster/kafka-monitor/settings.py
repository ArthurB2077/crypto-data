import os


def str2bool(v):
    return str(v).lower() in ("true", "1") if type(v) == str else bool(v)


# Redis host information
REDIS_DB = int(os.getenv("REDIS_DB", 0))
REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD", None)
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
REDIS_SOCKET_TIMEOUT = int(os.getenv("REDIS_SOCKET_TIMEOUT", 10))

# Kafka server information
KAFKA_CONSUMER_AUTO_COMMIT_ENABLE = True
KAFKA_CONSUMER_AUTO_OFFSET_RESET = "earliest"
KAFKA_CONSUMER_COMMIT_INTERVAL_MS = 5000
KAFKA_CONSUMER_FETCH_MESSAGE_MAX_BYTES = 10 * 1024 * 1024  # 10MB
KAFKA_CONSUMER_TIMEOUT = 50
KAFKA_FEED_TIMEOUT = 10
KAFKA_GROUP = os.getenv("KAFKA_GROUP", "demo-group")
KAFKA_HOSTS = [x.strip() for x in os.getenv("KAFKA_HOSTS", "kafka:9092").split(",")]
KAFKA_INCOMING_TOPIC = os.getenv("KAFKA_INCOMING_TOPIC", "demo.incoming")
KAFKA_PRODUCER_BATCH_LINGER_MS = 25  # 25 ms before flush
KAFKA_PRODUCER_BUFFER_BYTES = 4 * 1024 * 1024  # 4MB before blocking

# plugin setup
PLUGIN_DIR = "plugins/"
PLUGINS = {
    "plugins.scraper_handler.ScraperHandler": 100,
    "plugins.action_handler.ActionHandler": 200,
    "plugins.stats_handler.StatsHandler": 300,
    "plugins.zookeeper_handler.ZookeeperHandler": 400,
}

# logging setup
LOG_BACKUPS = 5
LOG_DIR = os.getenv("LOG_DIR", "logs")
LOG_FILE = "kafka_monitor.log"
LOG_JSON = str2bool(os.getenv("LOG_JSON", False))
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_MAX_BYTES = 10 * 1024 * 1024
LOG_STDOUT = str2bool(os.getenv("LOG_STDOUT", True))
LOGGER_NAME = "kafka-monitor"

# stats setup
STATS_CYCLE = 5
STATS_DUMP = 60
STATS_PLUGINS = str2bool(os.getenv("STATS_PLUGINS", True))
STATS_TOTAL = str2bool(os.getenv("STATS_TOTAL", True))
# from time variables in scutils.stats_collector class
STATS_TIMES = [
    "SECONDS_15_MINUTE",
    "SECONDS_1_HOUR",
    "SECONDS_6_HOUR",
    "SECONDS_12_HOUR",
    "SECONDS_1_DAY",
    "SECONDS_1_WEEK",
]

# main thread sleep time
HEARTBEAT_TIMEOUT = 120
SLEEP_TIME = 0.01
