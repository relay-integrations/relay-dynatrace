FROM relaysh/core:latest-python
RUN pip --no-cache-dir install quart
COPY "./handler.py" "/handler.py"
ENTRYPOINT []
CMD ["python3", "/handler.py"]

LABEL "org.opencontainers.image.title"="Dynatrace Problem Notification triggered"
LABEL "org.opencontainers.image.description"="This trigger fires when a Dynatrace problem notification webhook is triggered."
LABEL "com.puppet.nebula.sdk.version"="v1"
