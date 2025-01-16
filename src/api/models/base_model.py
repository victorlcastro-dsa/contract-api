from tortoise import fields
from tortoise.models import Model
from tortoise.timezone import now

class BaseModel(Model):
    """
    Base model with common fields and methods for all models.
    """
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    deleted_at = fields.DatetimeField(null=True, default=None)

    class Meta:
        abstract = True

    async def soft_delete(self):
        """
        Soft delete the record by setting the deleted_at field to the current time.
        """
        self.deleted_at = now()
        await self.save()

    async def restore(self):
        """
        Restore a soft-deleted record by setting the deleted_at field to None.
        """
        self.deleted_at = None
        await self.save()

    @classmethod
    def get_active(cls):
        """
        Get all active (non-deleted) records.
        """
        return cls.filter(deleted_at__isnull=True)

    def is_active(self):
        """
        Check if the record is active (not soft-deleted).
        """
        return self.deleted_at is None