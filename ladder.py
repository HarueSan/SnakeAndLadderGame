class Ladder:

    def __init__(self, start: int, end: int) -> None:
        self.start = start
        self.end = end

    # debug
    def __repr__(self):
        return f"start:<{self.start}, end:<{self.end}>"
    
    def validate_ladder(self):
        # จุดเริ่มต้นต้องน้อยกว่าจุดสิ้นสุด
        # จุดสิ้นสุดต้องมากกว่าจุดเริ่มต้น
        # จุดเริ่มต้นบรรไดต้องมากกว่าจุดหนึ่ง
        # ตัวเลขต้องเป็นจำนวนเต็มบวกที่มากกว่าหนึ่ง
        # ของน้องบาสเขียนให้กำหนดจุดเริ่มต้นทีหลังได้

