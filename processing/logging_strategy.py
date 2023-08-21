from datetime import datetime


class LoggingStrategy:
    def log(self, message):
        pass


class TextFileLoggingStrategy:
    def log(self, message):
        now = datetime.now()
        log_message = format_log_message(message, now)

        log_file_name = now.strftime("%Y%m%d_uploads")

        with open(f"{log_file_name}.log", "a") as log_file:
            log_file.write(f"{log_message}\n")


class ConsoleLoggingStrategy:
    def log(self, message):
        now = datetime.now()
        log_message = format_log_message(message, now)
        print(log_message)


def format_log_message(message, now):
    file_name = message['file_name']
    user_id = message['user_id']
    user_name = message['user_name']

    log_message = f"{now.strftime('%Y-%m-%d %H:%M:%S')} File name: {file_name}, User ID: {user_id}, User Name: {user_name}"

    return log_message
