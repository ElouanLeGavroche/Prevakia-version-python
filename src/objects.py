import pygame

from src import son

BUTTON_FOLDER = "assets/boutons/"


def clear_rect(surface, rect):
    pygame.draw.rect(surface, (0, 0, 0, 0), rect)
    pygame.display.flip()


class Button:
    __all__ = {}

    def __init__(
        self,
        name:   str,
        size:   tuple,
        pos:    tuple = None,
        hidden: bool = False,
        func = None
    ):
        self.name = name
        self.size = size
        self.pos = pos
        self.func = func
        self.hidden = hidden

        self.normal = None
        self.pressed = None
        self.rect = None
        self.update()
        Button.__all__[name] = self

    def update(self, **kwargs):
        for k, v in kwargs.items():
            if k in self.__dict__:
                setattr(self, k, v)

        self.normal = pygame.transform.scale(pygame.image.load(f"{BUTTON_FOLDER}{self.name}.png"), self.size)
        
        try:
            self.pressed = pygame.transform.scale(pygame.image.load(f"{BUTTON_FOLDER}{self.name}_press.png"), self.size)
        except FileNotFoundError:
            print(
                "Warning: "
                f"Le bouton {self.name} ne possède pas d'image en cas de click "
                "(l'image sans click sera donc utilisé)"
            )
            self.pressed = self.normal
        self.rect = self.normal.get_rect()

        if self.pos:
            self.rect.x = self.pos[0]
            self.rect.y = self.pos[1]

    def draw(self, surface, pressed: bool = False, sound: bool = False):
        if not self.hidden:
            if pressed:
                surface.blit(self.pressed, self.rect)
                if sound:
                    son.menu.play() # bruitage de click de bouton
            else:
                surface.blit(self.normal, self.rect)

    @classmethod
    def get(cls, name: str):
        return cls.__all__[name]


class TextRender:
    __all__ = {}
    __fonts__ = {}

    def __init__(
        self,
        name:       str,
        font:       str,
        text:       str,
        size:       int = True,
        color:      tuple = (255, 255, 255),
        pos:        tuple = None,
        rectparams: dict = {},
        hidden:     bool = False,
        func = None
    ):
        self.name = name
        self.font = font
        self.text = text
        self.size = size
        self.color = color
        self.pos = pos
        self.rectparams = rectparams
        self.hidden = hidden
        self.func = func

        self.ismultiline = lambda: "\n" in self.text or isinstance(self.text, list)

        self.surface = None
        self.rect = None
        self.full_rect = None
        self.update()
        TextRender.__all__[name] = self

    def update(self, **kwargs):
        for k, v in kwargs.items():
            if k in self.__dict__:
                setattr(self, k, v)

        font = TextRender.__fonts__[self.font]
        rectparams = {
            k: (
                eval(v, TextRender.__all__)
                if isinstance(v, str)
                else
                v
            )
            for k, v in self.rectparams.items()
        }

        if self.ismultiline():
            self.text = self.text.splitlines()
            
            self.surface = []
            self.rect = []

            w, h = font.size(max(self.text))
            self.full_rect = pygame.Rect(*self.pos, w, len(self.text) * h)

            for i, line in enumerate(self.text):
                self.surface.append(font.render(line, self.size, self.color))
                self.rect.append((self.pos[0], self.pos[1] + h * i))
        else:
            self.surface = font.render(
                str(self.text),
                self.size,
                self.color
            )
            self.rect = self.surface.get_rect(**rectparams)
            self.full_rect = self.rect

            if self.pos:
                self.rect.center = self.pos

    def draw(self, surface):
        if not self.hidden:
            if self.ismultiline():
                for surf, rect in zip(self.surface, self.rect):
                    surface.blit(surf, rect)
            else:
                surface.blit(self.surface, self.rect)

    def hide(self, surface):
        self.hidden = True
        clear_rect(surface, self.full_rect)

    @classmethod
    def get(cls, name: str):
        return cls.__all__[name]

    @classmethod
    def setfonts(cls, fonts: list):
        cls.__fonts__ = fonts


class Image:
    def __init__(
        self,
        path: str,
        size: tuple,
        pos: tuple = None,
        hidden: bool = False
    ):
        self.path = path
        self.size = size
        self.pos = pos
        self.hidden = hidden

        self.name = None
        self.surface = None
        self.rect = None
        self.update()

    def update(self, **kwargs):
        for k, v in kwargs.items():
            if k in self.__dict__:
                setattr(self, k, v)

        self.name = self.path.split("/" if "/" in self.path else "\\")[-1].lower()
        self.surface = pygame.transform.scale(
            pygame.image.load(f"assets/{self.path}.png"),
            self.size
        )
        self.rect = self.surface.get_rect()

        if self.pos:
            self.rect.x = self.pos[0]
            self.rect.y = self.pos[1]

    def draw(self, surface):
        if not self.hidden:
            surface.blit(self.surface, self.rect)

    def hide(self, surface):
        self.hidden = True
        clear_rect(surface, self.rect)
