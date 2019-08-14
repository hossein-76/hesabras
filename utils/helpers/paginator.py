
class InvalidPage(Exception):
    pass

class Page:

    def __init__(self,object_list,number,paginator):
        self.objects = object_list
        self.number = number
        self.paginator = paginator

    def __repr__(self):
        return '<Page {} of {}>'.format(self.number,self.paginator.num_pages)

    def __len__(self):
        return self.objects.__len__()

    def has_next(self):
        return self.number < self.paginator.num_pages

    def has_previous(self):
        return self.number > 1

    def has_other_pages(self):
        return self.has_previous() or self.has_next()

    def next_page_number(self):
        return self.paginator.page_validation(self.number + 1)

    def previous_page_number(self):
        return self.paginator.page_validation(self.number - 1)


class Paginator:
    def __init__(self,objects,data_limit=10):
        self.object_list = objects
        self.data_limit = int(data_limit)

    def page_validation(self,number):
        if number > 50:
            raise InvalidPage()
        try:
            if isinstance(number, float) and not number.is_integer():
                raise InvalidPage()
            number = int(number)
        except TypeError:
            raise InvalidPage()
        if number < 1:
            raise InvalidPage()
        if number > self.num_pages:
            if number == 1:
                pass
            else:
                raise InvalidPage()
        return number

    def page(self,number=1):
        number = self.page_validation(number)
        bottom = (number - 1) * self.data_limit
        top = bottom + self.data_limit
        if top >= self.count:
            top = self.count
        return Page(self.object_list[bottom:top], number, self)

    @property
    def count(self):
        return self.object_list.__len__()

    @property
    def num_pages(self):
        if self.count <= self.data_limit:
            return 1
        objects = max(1,self.count)
        return int(objects / self.data_limit) + 1
