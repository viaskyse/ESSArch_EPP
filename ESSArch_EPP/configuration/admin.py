#!/usr/bin/env /ESSArch/python27/bin/python
# -*- coding: UTF-8 -*-
'''
    ESSArch Tools - ESSArch is an Electronic Preservation Platform
    Copyright (C) 2005-2013  ES Solutions AB

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

    Contact information:
    Web - http://www.essolutions.se
    Email - essarch@essolutions.se
'''

from configuration.models import LogEvent, Parameter, SchemaProfile, Path, IPParameter, ESSArchPolicy, ESSConfig, ESSProc
from django.contrib import admin

# Logevents
class LogEventAdmin( admin.ModelAdmin ):
    list_display = ( 'eventDetail', 'eventType' )
    search_fields = ( 'eventDetail', )
        
admin.site.register( LogEvent, LogEventAdmin )
 
# XML schemas and namespaces
class SchemaProfileAdmin( admin.ModelAdmin ):
    list_display = ( 'entity', 'value' )
    search_fields = ( 'entity', )
    readonly_fields = ('entity',)
    fields = ('entity', 'value')
    
admin.site.register(SchemaProfile, SchemaProfileAdmin)

# Parameters
class ParameterAdmin( admin.ModelAdmin ):
    list_display = ( 'entity', 'value' )
    search_fields = ( 'entity', )
    readonly_fields = ('entity',)
    fields = ('entity', 'value')

admin.site.register(Parameter, ParameterAdmin)

# Paths
class PathAdmin( admin.ModelAdmin ):
    list_display = ( 'entity', 'value' )
    search_fields = ( 'entity', )
    readonly_fields = ('entity',)
    fields = ('entity', 'value')

admin.site.register(Path, PathAdmin)

# General metadata for information package
class IPParameterAdmin( admin.ModelAdmin ):
    list_display = ( 'type', 'label', 'createdate', 'recordstatus', 'deliverytype' )
    search_fields = ( 'type', )
    readonly_fields = ('objid',)
    list_filter = ('type', 'label')
    fieldsets = (
                (None,{
                   'classes': ('wide'),
                   'fields': (
                              'label',
                              'type',
                              'objid',
                              'createdate',
                              'recordstatus',
                              'deliverytype'
                              )}),
                ('General metadata for information package',{
                   'classes': ('collapse','wide'),
                   'fields': (
                              'deliveryspecification',
                              'submissionagreement',
                              'previoussubmissionagreement',
                              'datasubmissionsession',
                              'packagenumber',
                              'referencecode',
                              'previousreferencecode',
                              'appraisal',
                              'accessrestrict',
                              'archivist_organization',
                              'archivist_organization_id',
                              'archivist_organization_software',
                              'archivist_organization_software_id',
                              'creator_organization',
                              'creator_organization_id',
                              'creator_individual',
                              'creator_individual_details',
                              'creator_software',
                              'creator_software_id',
                              'editor_organization',
                              'editor_organization_id',
                              'preservation_organization',
                              'preservation_organization_id',
                              'preservation_organization_software',
                              'preservation_organization_software_id'
                              )}),
                ('Additional metadata for information package',{
                   'classes': ('collapse', 'wide'),
                   'fields': (
                              'startdate',
                              'enddate',
                              'aic_id',
                              'informationclass',
                              'projectname',
                              'policyid',
                              'receipt_email'
                              )}),
                )

admin.site.register(IPParameter, IPParameterAdmin)

# ESSArchPolicy
class ESSArchPolicyAdmin( admin.ModelAdmin ):
    list_display = ( 'PolicyName', 'PolicyID', 'PolicyStat', 'AISProjectName', 'AISProjectID', 'Mode' )
    fieldsets = (
                (None,{
                   'classes': ('wide'),
                   'fields': (
                              'PolicyName',
                              'PolicyID',
                              'PolicyStat',
                              'AISProjectName',
                              'AISProjectID',
                              'Mode',
                              'WaitProjectApproval',
                              'ChecksumAlgorithm',
                              'ValidateChecksum',
                              'ValidateXML',
                              'ManualControll',
                              'AIPType',
                              'AIPpath',
                              'PreIngestMetadata',
                              'IngestMetadata',
                              'INFORMATIONCLASS',
                              'IngestPath',
                              'IngestDelete',
                              )}),
                ('Storage method 1',{
                   'classes': ('collapse','wide'),
                   'fields': (
                              'sm_1',
                              'sm_type_1',
                              'sm_format_1',
                              'sm_blocksize_1',
                              'sm_maxCapacity_1',
                              'sm_minChunkSize_1',
                              'sm_minContainerSize_1',
                              'sm_minCapacityWarning_1',
                              'sm_target_1',
                              )}),
                ('Storage method 2',{
                   'classes': ('collapse','wide'),
                   'fields': (
                              'sm_2',
                              'sm_type_2',
                              'sm_format_2',
                              'sm_blocksize_2',
                              'sm_maxCapacity_2',
                              'sm_minChunkSize_2',
                              'sm_minContainerSize_2',
                              'sm_minCapacityWarning_2',
                              'sm_target_2',
                              )}),
                ('Storage method 3',{
                   'classes': ('collapse','wide'),
                   'fields': (
                              'sm_3',
                              'sm_type_3',
                              'sm_format_3',
                              'sm_blocksize_3',
                              'sm_maxCapacity_3',
                              'sm_minChunkSize_3',
                              'sm_minContainerSize_3',
                              'sm_minCapacityWarning_3',
                              'sm_target_3',
                              )}),
                ('Storage method 4',{
                   'classes': ('collapse','wide'),
                   'fields': (
                              'sm_4',
                              'sm_type_4',
                              'sm_format_4',
                              'sm_blocksize_4',
                              'sm_maxCapacity_4',
                              'sm_minChunkSize_4',
                              'sm_minContainerSize_4',
                              'sm_minCapacityWarning_4',
                              'sm_target_4',
                              )}),
                )

admin.site.register(ESSArchPolicy, ESSArchPolicyAdmin)

# ESSConfig (core)
class ESSConfigAdmin( admin.ModelAdmin ):
    list_display = ( 'Name', 'Value' )
    readonly_fields = ('Name',)
    fields = ('Name', 'Value')

admin.site.register(ESSConfig, ESSConfigAdmin)

# ESSProc (core)
class ESSProcAdmin( admin.ModelAdmin ):
    list_display = ( 'Name', 'Status', 'Run', 'PID', 'Pause' )
    readonly_fields = ('Name',)
    fields = ('Name', 'Path', 'LogFile', 'Time', 'Status', 'Run', 'PID', 'Pause')

admin.site.register(ESSProc, ESSProcAdmin)