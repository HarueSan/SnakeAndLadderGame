from player import Player
from board import Board

class Game:

    def __init__(self, player: Player, board: Board) -> None:
        self.board = board
        self.player = player

    def is_finish_game(self) -> bool:
        return self.player.position >= self.board.finish_line

    def start(self) -> None:
        # TODO: ลบเงื่อนไขบรรทัด 16 ออก เพราะตอนเริ่มเกมไม่จำเป็นต้องเช็คว่าจบเกมหรือยัง
        while not self.is_finish_game():
            dice_number = self.toss_dice() 
            self.move_forward(dice_number)
        
            if self.is_ladder_start():
                print("Lucky!! You found ladder")
                self.move_to_ladder_end()

            elif self.is_snake_head():
                print("Unlucky!! You were bitten by snake")
                self.move_to_snake_tail()
            
            print(f"Your current position is {self.player.position}")

        print("end game")

    # TODO: เปลี่ยนการทอยลูกเต๋าให้เป็นแบบสุ่ม ไม่ใช่รับมาจากข้างนอก     
    def toss_dice(self) -> int:
        return int(input("Dice: "))
            
    def move_forward(self, dice_number: int) -> None:
        self.player.position += dice_number
     
     # TODO: ให้ฟังก์ชันนี้ย้ายตำแหน่งผู้เล่นอย่างเดียว ไม่มีการเช็คว่ามีงูก่อน
    def move_to_snake_tail(self) -> None:
        snake = self.board.get_snake_at_current_position(self.player.position)

        if snake:
            self.player.position = snake.tail
    
    # TODO: ให้ฟังก์ชันนี้ย้ายตำแหน่งผู้เล่นอย่างเดียว ไม่มีการเช็คว่ามีบรรไดก่อน
    def move_to_ladder_end(self) -> None:
        ladder = self.board.get_ladder_at_current_position(self.player.position)

        if ladder:
            self.player.position = ladder.end
     # TODO: เปลี่ยนชื่อฟังก์ชัน board.get_snake_at_current_position ไม่ต้องมีคำว่า current
    def is_snake_head(self) -> bool:
        if self.board.get_snake_at_current_position(self.player.position):
            return True
        
        return False
    # TODO: เปลี่ยนชื่อฟังก์ชัน board.get_ladder_at_current_position ไม่ต้องมีคำว่า current 
    def is_ladder_start(self) -> bool:
        if self.board.get_ladder_at_current_position(self.player.position):
            return True
        
        return False
        