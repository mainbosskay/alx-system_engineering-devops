#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - Staring an infinite loop
 * Return: it is 0 if loop is interrupted
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * createzombie - Creating new child process and print PID
 * Return: it is void
 */

void createzombie(void)
{
	int chld_pid = fork();

	if (chld_pid == 0)
	{
		printf("Zombie process created, PID: %d\n", getpid());
		exit(0);
	}
}

/**
 * main - Creating 5 zombies
 * Return: it is 0 on success
 */

int main(void)
{
	createzombie();
	createzombie();
	createzombie();
	createzombie();
	createzombie();
	return (infinite_while());
}
