FROM amazonlinux:2 as awscli-installer
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
RUN yum update -y \
  && yum install -y unzip \
  && unzip awscliv2.zip \
  && ./aws/install --bin-dir /aws-cli-bin/


FROM jenkins/agent
COPY --from=docker /usr/local/bin/docker /usr/local/bin/
COPY --from=awscli-installer /usr/local/aws-cli/ /usr/local/aws-cli/
COPY --from=awscli-installer /aws-cli-bin/ /usr/local/bin/

RUN curl https://static.snyk.io/cli/v1.666.0/snyk-linux -o snyk && chmod +x ./snyk && mv ./snyk /usr/local/bin/
