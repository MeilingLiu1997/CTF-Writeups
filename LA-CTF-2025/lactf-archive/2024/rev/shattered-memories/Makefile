CC=gcc
CFLAGS=-Wall -Wpedantic -Werror -O0

NAME=shattered-memories

.PHONY: clean run build

$(NAME): $(NAME).c
	docker run --rm -u "$(shell id -u):$(shell id -g)" -v "$(CURDIR):/app" -w /app buildpack-deps:bookworm $(CC) $(NAME).c -I. $(CFLAGS) -o $(NAME)

build: $(NAME)

clean:
	rm $(NAME)

run: build
	./$(NAME)
