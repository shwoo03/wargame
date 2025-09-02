FROM ubuntu:22.04@sha256:27cb6e6ccef575a4698b66f5de06c7ecd61589132d5a91d098f7f3f9285415a9

ENV user chall
ENV chall_port 31337

RUN apt-get update
RUN apt-get install -y python3

RUN adduser $user

COPY ./deploy/flag /home/$user/flag

RUN chown -R root:$user /home/$user

WORKDIR /home/chall
RUN touch `python3 -c "print(open('./flag', 'r').read())"`
RUN rm *

WORKDIR /home
USER $user
EXPOSE $chall_port