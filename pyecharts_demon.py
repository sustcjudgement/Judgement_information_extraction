from pyecharts import options as opts
from pyecharts.charts import Geo,Bar
from pyecharts.charts import Map


def test():
    x = ["laoban","yuangong"]
    for i in range(len(x)):
        if x[i] is "广西壮族自治":
            x[i]  = "广西"
    y = [12,20]
    # print( dict(zip(x,y)))
    c = (
        Bar()
            .add_xaxis(x)
            .add_yaxis("职位",y)
            # .add_yaxis("商家B", Faker.values())
            .set_global_opts(title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题"))
    )
    c.render(path="hhh.html")

if __name__ == '__main__':
    test()