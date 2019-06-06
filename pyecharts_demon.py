from pyecharts import options as opts
from pyecharts.charts import Geo,Bar
from pyecharts.charts import Map


def test()->Geo:
    x = ['浙江', ]
    m = []
    n = "浙江省"
    print(n[:-1])
    if len(m) is 0:
        print(True)
    y = [29]
    print(len(x),len(y))
    c = (
        Geo()
            .add_schema(maptype="china")
            .add("geo", [list(z) for z in zip(x,y)])
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(is_piecewise=True),
            title_opts=opts.TitleOpts(title="Geo-基本示例"),
        )
    )
    c.render()

if __name__ == '__main__':
    test()