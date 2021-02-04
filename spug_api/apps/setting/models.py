# Copyright: (c) OpenSpug Organization. https://github.com/openspug/spug
# Copyright: (c) <spug.dev@gmail.com>
# Released under the AGPL-3.0 License.
from django.db import models
from libs import ModelMixin


class Setting(models.Model, ModelMixin):
    key = models.CharField(max_length=50, unique=True)
    value = models.TextField()
    desc = models.CharField(max_length=255, null=True)

    def __repr__(self):
        return '<Setting %r>' % self.key
    
#db_table：用来指定model对应的数据库中的表名，若不指定，Django会自动生成相应的表名，但是，自动生成的表名的可读性就不能够保证了。
    class Meta:
        db_table = 'settings'
