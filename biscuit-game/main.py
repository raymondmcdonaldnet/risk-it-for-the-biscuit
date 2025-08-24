import pygame

def main():
	pygame.init()

	screen = pygame.display.set_mode((1280, 720))
	clock = pygame.Clock()
	# Delta time in seconds.
	dt = 0

	# Game loop
	while True:
		# Handle events.
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		# Update.
		pass

		# Draw.
		# Fill the screen with a very obvious color so we know when something is wrong with drawing.
		screen.fill((255, 0, 255))
		pygame.display.flip()

		# Handle game time.
		dt = clock.tick(60) / 1000


if __name__ == "__main__":
	main()
