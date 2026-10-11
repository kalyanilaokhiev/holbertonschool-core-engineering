#!/usr/bin/env python3


class VerboseList(list):
    def append(self, item):
        super().append(item)
        print("Added{} to the list.".format(item))

    def extend(self, item):
        super().extend(item)
        print("Extended the list with {} items".format(item))

    def remove(self, item):
        super().remove(item)
        print("Removed [item] from the list.".format(item))

    def pop(self, index=-1):
        # get item before removal
        item = self[index]
        print("Popped {} from the list.".format(item))
        # remove and return the item
        return super().pop(index)


vl = VerboseList([1, 2, 3])
vl.append(4)
vl.extend([5, 6])
vl.remove(2)
vl.pop()
vl.pop(0)
