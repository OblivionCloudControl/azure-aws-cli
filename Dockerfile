FROM python:2.7.12-alpine

MAINTAINER Steyn Huizinga <steyn@oblcc.com>

ADD setup.py bin/ /tmp/azure-aws-cli/
ADD bin/aad_aws_login /tmp/azure-aws-cli/bin/

RUN apk add --no-cache --virtual .azure-aws-cli-rundeps \
    build-base && \
    pip install -U pip && \
    mkdir -p /tmp/azure-aws-cli && \
    pip install /tmp/azure-aws-cli/ && \
    apk del .azure-aws-cli-rundeps && \
    rm -Rf /tmp/azure-aws-cli/

ENTRYPOINT ["/usr/local/bin/aad_aws_login"]
