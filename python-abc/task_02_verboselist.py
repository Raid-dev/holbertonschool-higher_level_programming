#!/usr/bin/env python3
class VerboseList(list):

    def append(self, item):
        super().append(item)
        print(f"Added {[item]} to the list.")

    def extend(self, iterable):
        items_added = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with {[items_added]} items.")

    def remove(self, item):
        print(f"Removed {[item]} from the list.")
        super().remove(item)

    def pop(self, index=-1):
        item = self[index]
        print(f"Popped {[item]} from the list.")
        return super().pop(index)
