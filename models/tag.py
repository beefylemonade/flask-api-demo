from db import db


class TagModel(db.Model):
    __tablename__ = "tags"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"), nullable=False)

    store = db.relationship("StoreModel", back_populates="tags")

    items = db.relationship("ItemModel", back_populates="tags", secondary="items_tags")

    # this makes sure that the pair name and store_id need to be uniqe

    __table_args__ = (
        db.UniqueConstraint("name", "store_id", name="_name_store_uc"),
    )
