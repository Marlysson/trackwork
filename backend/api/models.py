from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        db_table = 'project'


class Task(models.Model):

    status_types = (
        ('STOPPED', 'Stopped'),
        ('WORKING', 'Working')
    )

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    
    description = models.CharField(max_length=255, null=False, blank=False)
    hours_worked = models.DurationField(default=None, null=True)
    status = models.CharField(max_length=7, choices=status_types)

    class Meta:
        db_table = 'task'


class Progress(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    
    requested_in = models.DateField(default=None)
    started_in = models.DateField(default=None)
    expected_conclusion = models.DateField(default=None)
    done_in = models.DateField(default=None)

    class Meta:
        db_table = 'progress'


class CheckList(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    class Meta:
        db_table = 'checklist'


class ItemCheckList(models.Model):
    checklist = models.ForeignKey(CheckList, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, null=False, blank=False)
    done = models.BooleanField(default=False)

    class Meta:
        db_table = 'itemchecklist'