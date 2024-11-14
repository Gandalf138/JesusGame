import pygame
from pygame.locals import VIDEORESIZE  # TODO resize
import random
from data.audio import musicfile, hit_sound_files
from data.font import font as default_font
from data.graphics import Bucket, Cross, Jesus, NailFull, NailHead, Reset


pygame.init()
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)  # TODO pygame.RESIZABLE
pygame.display.set_caption("Jesus Game")

music = pygame.mixer.Sound(musicfile)
music.play(loops=-1)

hit_sounds = [pygame.mixer.Sound(file) for file in hit_sound_files]

background = pygame.Surface(window_size)
background.fill("DarkGrey")

state = {"game_state": 0, "nail_count": 1, "nail_held": False}

NAILS_ALLOWED = 5


def play_random_hit_sound():
    hit_sounds[random.randint(0, len(hit_sounds)) - 1].play()


class Sprite:
    def __init__(self, surf: str, rotation_angle: float | None = None, **kwargs):
        self.surf = pygame.image.load(surf).convert_alpha()
        self.rect = self.surf.get_rect(**kwargs)
        if rotation_angle:
            self.rotate(rotation_angle)

    def draw(self, surface=screen):
        surface.blit(self.surf, self.rect)

    def rotate(self, angle: float):
        self.rotation_angle = angle
        self.surf = pygame.transform.rotate(self.surf, angle).convert_alpha()

    def resize(self):
        (resize_w, resize_h) = event.dict["size"]
        scale_ratios = (resize_w / window_size[0], resize_h / window_size[1])
        self.surf = pygame.transform.scale_by(
            self.surf,
            scale_ratios,
        )
        self.rect = self.surf.get_rect(topleft=self.rect.topleft)

    def is_on(self, y: "Sprite") -> bool:
        return (
            self.rect.left >= y.rect.left
            and self.rect.right <= y.rect.right
            and self.rect.top >= y.rect.top
            and self.rect.bottom <= y.rect.bottom
        )


class Text(Sprite):
    def __init__(
        self,
        size: int,
        text: str | bytes,
        color: pygame.color.Color | int | str | tuple[int, int, int],
        **kwargs
    ):
        self.font = pygame.font.Font(default_font, size)
        self.surf = self.font.render(text, False, color)
        self.rect = self.surf.get_rect(**kwargs)


class TitleText(Text):
    def __init__(self, text: str | bytes, **kwargs):
        self.font = pygame.font.Font(default_font, 45)
        self.surf = self.font.render(text, False, "Black")
        self.rect = self.surf.get_rect(center=(400, 50))


cross = Sprite(Cross, center=(400, 300))
jesus = Sprite(Jesus, 90, midleft=(0, 560))

bucket = Sprite(Bucket, bottomleft=(5, 595))
nail_full = Sprite(NailFull)
nails = [Sprite(NailHead) for _ in range(NAILS_ALLOWED)]

reset_button = Sprite(Reset, bottomright=(795, 595))

text_place = TitleText("Place Jesus on the Cross")
text_nail = TitleText("Nail Jesus to the Cross")
text_label = Text(20, "NAILS", "Red", midbottom=bucket.rect.midbottom)


def draw_scene(sprites: list[Sprite], surface=screen):
    for sprite in sprites:
        sprite.draw(surface)


def resize_screen():
    global background
    global window_size
    background = pygame.transform.scale(background, event.dict["size"])
    sprites = [
        cross,
        jesus,
        bucket,
        nail_full,
        *nails,
        reset_button,
        text_place,
        text_nail,
        text_label,
    ]
    for sprite in sprites:
        sprite.resize()
    window_size = event.dict["size"]
    pygame.display.update()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == VIDEORESIZE:
            resize_screen()

    screen.blit(background, (0, 0))
    mouse_pos = pygame.mouse.get_pos()
    lmb_pressed = pygame.mouse.get_pressed()[0]

    if state["game_state"] == 0:
        if jesus.rect.collidepoint((mouse_pos)) and lmb_pressed:
            jesus.rotate(-90)
            state["game_state"] += 1
        draw_scene([cross, text_place, jesus])
    elif state["game_state"] == 1:
        if lmb_pressed:
            jesus.rect.center = mouse_pos
        else:
            if jesus.is_on(cross):
                jesus.rect.center = (cross.rect.center[0], cross.rect.center[1] + 45)
                state["game_state"] += 1
        draw_scene([cross, text_place, jesus])
    else:
        nails_in_scene = nails[: state["nail_count"] - 1]
        draw_scene([bucket, cross, text_nail, text_label, jesus, *nails_in_scene])

        if bucket.rect.collidepoint((mouse_pos)) and lmb_pressed:
            state["nail_held"] = True

        if state["nail_held"] and state["nail_count"] <= NAILS_ALLOWED:
            nail_full.rect.midbottom = mouse_pos
            nail_full.draw()
            if not lmb_pressed:
                if jesus.rect.collidepoint((mouse_pos)):
                    play_random_hit_sound()
                    nails[state["nail_count"] - 1].rect.midbottom = mouse_pos
                    nails[state["nail_count"] - 1].draw()
                    state["nail_count"] += 1
                state["nail_held"] = False

        if state["nail_count"] > NAILS_ALLOWED:
            reset_button.draw()
            if reset_button.rect.collidepoint((mouse_pos)) and lmb_pressed:
                state["nail_count"] = 1

    pygame.display.update()


pygame.quit()
