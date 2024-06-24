from fastapi import APIRouter, Path

router = APIRouter(prefix="/items", tags=["items"])

@router.get("/")
def list_items():
    return [
        "Item1",
        "Item2",
        "Item3",
    ]


@router.get("/latest/")
def get_latest_item():
    return {"item": {"id": "0", "name": "latest"}}


@router.get("/{item_id}/")
def get_item_by_id(item_id: int | None = Path(ge=1, lt=1_000_000)):
    return {
        "item": {
            "id": item_id,
        },
    }