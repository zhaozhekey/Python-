# 房子(House) 有 户型、总面积 、剩余面积(等于总面积的60%) 和 家具名称列表 属性
# 新房子没有任何的家具
# 将 家具的名称 追加到 家具名称列表 中
# 判断 家具的面积 是否 超过剩余面积，如果超过，提示不能添加这件家具

# 家具(Furniture) 有 名字 和 占地面积属性，其中
# 席梦思(bed) 占地 4 平米
# 衣柜(chest) 占地 2 平米
# 餐桌(table) 占地 1.5 平米
# 将以上三件 家具 添加 到 房子 中
# 打印房子时，要求输出：户型、总面积、剩余面积、家具名称列表

class House(object):
    def __init__(self, house_type, total_area, furn_list=None):
        if furn_list is None:
            furn_list = []
        self.house_type = house_type
        self.total_area = total_area
        self.free_area = total_area * 0.6
        self.furn_list = furn_list

    def add_furn(self):
        pass


class Furniture(object):
    def __init__(self, name, area):
        self.name = name
        self.area = area


house = House("两室一厅", 80)

# 席梦思(bed) 占地 4 平米
# 衣柜(chest) 占地 2 平米
# 餐桌(table) 占地 1.5 平米

bed = Furniture("席梦思", 4)
chest = Furniture("衣柜", 2)
table = Furniture("餐桌", 1.5)
sofa = Furniture("沙发", 12)
