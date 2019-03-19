import yaml


def read_data():
    with open("./data/data.yaml","r",encoding="utf-8") as f:
        datas = yaml.load(f)
        return datas

# if __name__ == '__main__':
#     print(read_data())