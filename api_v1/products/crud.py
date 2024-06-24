from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result

from core.models import Product
from .schemas import ProductCreate, ProductUpdate, ProductPartial


async def get_products(session: AsyncSession) -> list[Product]:
    stmt = select(Product).order_by(Product.id)
    result: Result = await session.execute(stmt)
    products = result.scalars().all()
    return list(products)


async def get_product(session: AsyncSession, product_id: int) -> Product | None:
    return await session.get(Product, product_id)


async def create_product(session: AsyncSession, product_in: ProductCreate):
    product = Product(**product_in.model_dump())
    session.add(product)
    await session.commit()
    # await session.refresh(product)
    return product


async def update_product(session: AsyncSession, product: Product, product_update: ProductUpdate) -> Product:
    for name, value in product_update.model_dump():
        setattr(product, name, value)
    await session.commit()
    return product


async def update_product_part1(session: AsyncSession, product: Product, product_update: ProductPartial):
    for name, value in product_update.model_dump(exclude_unset=True):
        setattr(product, name, value)
    await session.commit()
    return product
