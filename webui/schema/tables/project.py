#!/usr/bin/env python
# -*- coding:utf-8 -*-

from sqlalchemy import and_
from sqlalchemy import Column, BOOLEAN, VARCHAR, INT
from sqlalchemy.sql import func

from schema.tables.base import BaseTable
from common.utils import guid


class Project(BaseTable):

    __tablename__ = 'project'

    uid = Column(VARCHAR(32), primary_key=True, default=guid)
    name = Column(VARCHAR(200))
    target = Column(VARCHAR(200))
    desc = Column(VARCHAR(1000))

    @classmethod
    def add(cls, name, target, desc):
        p = Project()
        p.name = name
        p.target = target
        p.desc = desc
        cls.db.add(p)
        cls.db.commit()
        return True
