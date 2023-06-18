def domain_name(url):
    # if "://" in url:
    #     for i in url.split("://"):
    #         if "." in i:
    #             res = i.split(".")
    #             return res[0] if "www" not in res else res[1]
    # return url.split(".")[1] if "www" in url.split(".") else url.split(".")[0]

    return url.split("//")[-1].split("www.")[-1].split(".")[0]


print(domain_name("http://google.com"))
print(domain_name("http://google.co.jp"))
print(domain_name("www.xakep.ru"))
print(domain_name("http://github.com/carbonfive/raygun"))
print(domain_name("https://youtube.com"))
print(domain_name("http://www.u8w9f5htwsueyfmz2g3g624zzgof.tv/"))
print(domain_name("vlpsjnx4j8dmrqy0yai996ngy.co.uk"))
