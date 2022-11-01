from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        opened_rooms = set[int]([0])
        keys = set(rooms[0])
        if 0 in keys:
            keys.remove(0)
        while len(keys) > 0:
            key = keys.pop()
            opened_rooms.add(key)
            for new_key in rooms[key]:
                if new_key not in keys and new_key not in opened_rooms:
                    keys.add(new_key)
            if len(opened_rooms) == len(rooms):
                return True
        return False

