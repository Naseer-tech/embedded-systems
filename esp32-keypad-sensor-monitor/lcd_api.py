class LcdApi:
    LCD_CLR = 0x01
    LCD_HOME = 0x02

    def __init__(self, num_lines, num_columns):
        self.num_lines = num_lines
        self.num_columns = num_columns

    def clear(self):
        self.hal_write_command(self.LCD_CLR)

    def move_to(self, cursor_x, cursor_y):
        addr = cursor_x & 0x3F
        if cursor_y & 1:
            addr += 0x40
        self.hal_write_command(0x80 | addr)

    def putchar(self, char):
        self.hal_write_data(ord(char))

    def putstr(self, string):
        for char in string:
            self.putchar(char)