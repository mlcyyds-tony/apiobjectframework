------

### 📖 项目简介

这是一个基于 **API Object 设计模式** 的接口自动化测试框架，专门针对公开商城练习靶场（MTXShop）设计，欢迎大家进行二次开发！

- **技术栈**：Python + Pytest + Requests
- **覆盖范围**：买家、卖家、管理员三端接口全覆盖
- **核心功能**：多环境配置、数据驱动、并行执行、Allure 报告、数据库/Redis 验证。

### ✅ 核心特点

- **设计模式**：API Object 模式，接口封装与测试逻辑分离，易于维护。
- **多角色支持**：支持买家、卖家、管理员三端接口测试。
- **多环境管理**：支持 SIT/UAT/TEST 等环境快速切换。
- **数据驱动**：支持 Excel/YAML 数据源，数据与代码分离。
- **高效执行**：基于 pytest-xdist 实现多进程并发。
- **完整报告**：集成 Allure 报告，提供清晰的结果展示。
- **数据库/Redis**：支持 MySQL 数据校验与 Redis 缓存操作。
- **安全支持**：集成 AES ECB 加密解密工具。


### ✅ todolist
- [ ] 完善测试用例，覆盖更多业务场景。
- [ ] 添加mock功能，模拟接口响应。
- [ ] 集成Pipeline，实现测试持续集成。
- [ ] 完善Allure个性化定制，提供更详细的测试结果展示。

------

### 🏗️ 项目架构

项目目录结构清晰，分为接口层、公共工具层、配置层、测试数据层和测试用例层。

```text
apiobjectframework/
├── api/                 # 接口层：封装具体业务接口
│   ├── base_api.py      # 基类定义
│   ├── buyer/           # 买家端接口 (登录、购物车、订单等)
│   ├── seller/          # 卖家端接口 (商品管理、订单管理)
│   └── manager/         # 管理员端接口 (商品审核)
├── common/              # 公共工具层
│   ├── client.py        # HTTP 请求客户端
│   ├── db_util.py       # MySQL 工具
│   ├── redis_util.py    # Redis 工具
│   ├── logger.py        # 日志工具
│   └── ...              # 加密、文件加载等工具
├── config/              # 配置层
│   ├── env_test.yml     # 测试环境配置
│   ├── env_sit.yml      # SIT 环境配置
│   ├── http.yml         # HTTP 地址配置
│   └── db.yml           # 数据库配置
├── data/                # 测试数据层
│   ├── mtxshop_data.xlsx # Excel 数据源
│   └── mtxshop_data.yml  # YAML 数据源
├── testcases/           # 测试用例层
│   ├── buyer/           # 买家端用例 (立即购买、加入购物车等)
│   ├── seller/          # 卖家端用例 (商品管理)
│   └── business_flow/   # 业务流程测试 (完整订单流程)
├── logs/                # 日志存储
├── report/data/         # Allure 报告数据
├── run.py               # 测试执行入口
└── pytest.ini           # Pytest 配置文件
```

------

### 🚀 快速开始

#### 1. 环境要求

- Python 3.7+
- MySQL 数据库
- Redis (可选)
- Allure Commandline (需 Java 环境)

#### 2. 安装依赖

```bash
# 1. 克隆项目
git clone https://github.com/mlcyyds/apiobjectframework.git
cd apiobjectframework

# 2. 安装 Python 依赖
pip install -r requirements.txt

# 3. 安装 Allure (参考网上教程)
```

#### 3. 配置环境

修改 `config/` 目录下的配置文件（如 `env_test.yml`）：

- **账号密码**：配置买家、卖家、管理员的默认账号密码。
- **服务地址**：修改 HTTP 请求的 Host 地址。
- **数据库/Redis**：填写对应的连接信息。

#### 4. 运行测试

通过 `run.py` 指定环境运行：

```bash
# 默认执行测试环境
python run.py

# 指定执行 SIT 环境
python run.py sit

# 指定执行 UAT 环境
python run.py uat
```

#### 5. 查看报告

测试结束后，自动打开浏览器展示 Allure 报告。也可手动执行：

```bash
# 生成并查看报告
allure serve report/data
```

------

### 💡 核心概念与开发指南

#### 1. API Object 设计模式

每个接口封装为独立类，继承自基类（如 `BaseBuyerApi`）。

```python
from api.base_api import BaseBuyerApi

class BuyNowApi(BaseBuyerApi):
    def __init__(self, sku_id):
        super().__init__()
        self.url = f'{self.host}/buyer/cart/buyNow'
        self.method = 'POST'
        self.json = {
            "skuId": sku_id,
            "num": 1
        }
```

#### 2. Token 自动管理

利用 Pytest Fixture 自动处理登录和 Token 注入：

- **机制**：在 `conftest.py` 中定义 `buyer_login` fixture。
- **效果**：所有买家接口自动携带 Token，无需在用例中重复处理。

#### 3. 数据驱动

支持从 Excel 或 YAML 读取数据：

```python
test_data = read_excel(mtxshop_data_xlsx, '立即购买测试数据')
@pytest.mark.parametrize('casename,sku_id,num,expect_status,expect_body', test_data)
def test_buy_now(self, casename, sku_id, num, expect_status, expect_body):
    # 测试逻辑
```

#### 4. 数据准备与清理 (Fixture)

利用 Fixture 的 `yield` 机制实现数据的“造数”与“清理”：

```python
@pytest.fixture(scope='class')
def goods_data(db_init):
    # 前置：添加并审核商品
    goods_id = add_and_audit_goods()
    sku_id = get_sku_id_from_db(goods_id)
    yield goods_id, sku_id
    # 后置：下架、回收、删除商品
    cleanup_goods(goods_id)
```

#### 5. 并行执行配置

在 `pytest.ini` 中配置：

- `-n 2`：启用 2 个进程并行。
- `--dist=loadfile`：按文件分配任务，保证同一文件的用例顺序执行。

------

### 📊 技术栈清单

| 技术库                   | 版本/用途 | 说明         |
| ------------------------ | --------- | ------------ |
| **Python**               | 3.7+      | 编程语言     |
| **Pytest**               | 7.3.1     | 核心测试框架 |
| **Requests**             | 2.31.0    | HTTP 请求库  |
| **PyMySQL**              | 1.1.0     | MySQL 操作   |
| **Redis**                | 4.6.0     | Redis 操作   |
| **Allure**               | 2.13.2    | 报告生成     |
| **pytest-xdist**         | -         | 并行执行     |
| **pytest-rerunfailures** | 11.1.2    | 失败重试     |
| **openpyxl**             | -         | Excel 读写   |

------

### ⚠️ 注意事项

1. **环境隔离**：请确保不同环境的配置文件（如数据库连接）互不干扰。
2. **数据清理**：测试用例结束后务必清理产生的脏数据，保持环境纯净。
3. **Token 有效期**：当前 Token 为 Session 级别，需注意过期时间。
4. **并行互斥**：涉及共享资源（如特定商品库存）的测试用例，需注意并行执行的冲突。
5. **权限配置**：确保数据库账号拥有足够的查询和操作权限。

Happy Testing! 🎉
