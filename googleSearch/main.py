import newsGetter


def main():
    pirates = newsGetter.NewsGetter("Pittsburgh Pirates")
    list = (pirates.getArticleInfo())
    print(list[0])


if __name__ == '__main__':
    main()

