from locators.quotes_locators import QuoteLocators


class QuoteParser:
    """
    Given one of the specific quote divs, find out the data about the quote (quote content, author and tags)
    """

    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'<Quote {self.content}, by {self.author}>'

    @property
    def content(self):
        locator = QuoteLocators.CONTENT
        return self.parent.select_one(locator).string

    @property
    def author(self):
        locator = QuoteLocators.AUTHOR
        return self.parent.select_one(locator).string

    @property
    def tags(self):
        locator = QuoteLocators.TAGS
        return self.parent.select(locator)

    @property
    def tag_list(self):
        if self.tags:
            tags_list = " || Tags: "
            for tag in self.tags:
                tags_list = f'{tags_list}{tag.string}, '
            tags_list = tags_list[:-2]
            return tags_list
        return ""
