<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
  <xsl:template match="/COMMENT">&lt;COMMENT&gt;&lt;xsl:apply-templates/&gt;&lt;/COMMENT&gt;</xsl:template>
  <xsl:template match="/None">&lt;None&gt;&lt;xsl:apply-templates/&gt;&lt;/None&gt;</xsl:template>
  <xsl:template match="/None">&lt;None&gt;&lt;xsl:apply-templates/&gt;&lt;/None&gt;</xsl:template>
  <xsl:template match="/None">&lt;None&gt;&lt;xsl:apply-templates/&gt;&lt;/None&gt;</xsl:template>
  <xsl:template match="/None">&lt;None&gt;&lt;xsl:apply-templates/&gt;&lt;/None&gt;</xsl:template>
  <xsl:template match="/None">&lt;None&gt;&lt;xsl:apply-templates/&gt;&lt;/None&gt;</xsl:template>
  <xsl:template match="/LABEL">&lt;LABEL&gt;&lt;xsl:apply-templates/&gt;&lt;/LABEL&gt;</xsl:template>
  <xsl:template match="/DEFINITION">&lt;DEFINITION&gt;&lt;xsl:apply-templates/&gt;&lt;/DEFINITION&gt;</xsl:template>
  <xsl:template match="/RIGHT">&lt;RIGHT&gt;&lt;xsl:apply-templates/&gt;&lt;/RIGHT&gt;</xsl:template>
  <xsl:template match="/OBLIGATION">&lt;OBLIGATION&gt;&lt;xsl:apply-templates/&gt;&lt;/OBLIGATION&gt;</xsl:template>
  <xsl:template match="/PERMISSION">&lt;PERMISSION&gt;&lt;xsl:apply-templates/&gt;&lt;/PERMISSION&gt;</xsl:template>
  <xsl:template match="/PROHIBITION">&lt;PROHIBITION&gt;&lt;xsl:apply-templates/&gt;&lt;/PROHIBITION&gt;</xsl:template>
  <xsl:template match="/PENALTY">&lt;PENALTY&gt;&lt;xsl:apply-templates/&gt;&lt;/PENALTY&gt;</xsl:template>
  <xsl:template match="/REPARATION">&lt;REPARATION&gt;&lt;xsl:apply-templates/&gt;&lt;/REPARATION&gt;</xsl:template>
  <xsl:template match="/None">&lt;None&gt;&lt;xsl:apply-templates/&gt;&lt;/None&gt;</xsl:template>
  <xsl:template match="/EXCEPTION">&lt;EXCEPTION&gt;&lt;xsl:apply-templates/&gt;&lt;/EXCEPTION&gt;</xsl:template>
  <xsl:template match="/EXCEPT">&lt;EXCEPT&gt;&lt;xsl:apply-templates/&gt;&lt;/EXCEPT&gt;</xsl:template>
  <xsl:template match="/COMPLEMENT">&lt;COMPLEMENT&gt;&lt;xsl:apply-templates/&gt;&lt;/COMPLEMENT&gt;</xsl:template>
  <xsl:template match="/POWER">&lt;POWER&gt;&lt;xsl:apply-templates/&gt;&lt;/POWER&gt;</xsl:template>
  <xsl:template match="/ATTRIBUTION">&lt;ATTRIBUTION&gt;&lt;xsl:apply-templates/&gt;&lt;/ATTRIBUTION&gt;</xsl:template>
  <xsl:template match="/TEXT_IDENTIFIER">&lt;TEXT_IDENTIFIER&gt;&lt;xsl:apply-templates/&gt;&lt;/TEXT_IDENTIFIER&gt;</xsl:template>
  <xsl:template match="/DICTIONARY">&lt;DICTIONARY&gt;&lt;xsl:apply-templates/&gt;&lt;/DICTIONARY&gt;</xsl:template>
  <xsl:template match="/None">&lt;None&gt;&lt;xsl:apply-templates/&gt;&lt;/None&gt;</xsl:template>
  <xsl:template match="/None">&lt;None&gt;&lt;xsl:apply-templates/&gt;&lt;/None&gt;</xsl:template>
  <xsl:template match="/None">&lt;None&gt;&lt;xsl:apply-templates/&gt;&lt;/None&gt;</xsl:template>
  <xsl:template match="/None">&lt;None&gt;&lt;xsl:apply-templates/&gt;&lt;/None&gt;</xsl:template>
  <xsl:template match="/CONCEPT_ENTRY">&lt;CONCEPT_ENTRY&gt;&lt;xsl:apply-templates/&gt;&lt;/CONCEPT_ENTRY&gt;</xsl:template>
  <xsl:template match="/CONCEPT">&lt;CONCEPT&gt;&lt;xsl:apply-templates/&gt;&lt;/CONCEPT&gt;</xsl:template>
  <xsl:template match="/LEGAL_ENTITY_ENTRY">&lt;LEGAL_ENTITY_ENTRY&gt;&lt;xsl:apply-templates/&gt;&lt;/LEGAL_ENTITY_ENTRY&gt;</xsl:template>
  <xsl:template match="/LEGAL_ENTITY">&lt;LEGAL_ENTITY&gt;&lt;xsl:apply-templates/&gt;&lt;/LEGAL_ENTITY&gt;</xsl:template>
  <xsl:template match="/PERSON_ENTRY">&lt;PERSON_ENTRY&gt;&lt;xsl:apply-templates/&gt;&lt;/PERSON_ENTRY&gt;</xsl:template>
  <xsl:template match="/PERSON">&lt;PERSON&gt;&lt;xsl:apply-templates/&gt;&lt;/PERSON&gt;</xsl:template>
  <xsl:template match="/ABSTRACT_ENTITY_ENTRY">&lt;ABSTRACT_ENTITY_ENTRY&gt;&lt;xsl:apply-templates/&gt;&lt;/ABSTRACT_ENTITY_ENTRY&gt;</xsl:template>
  <xsl:template match="/@is_list_header">&lt;xsl:value-of select="@is_list_header"/&gt;</xsl:template>
  <xsl:template match="/@has_list_header">&lt;xsl:value-of select="@has_list_header"/&gt;</xsl:template>
  <xsl:template match="/@lang">&lt;xsl:value-of select="@lang"/&gt;</xsl:template>
  <xsl:template match="/@value">&lt;xsl:value-of select="@value"/&gt;</xsl:template>
  <xsl:template match="/@IDENTIFIER">&lt;xsl:value-of select="@IDENTIFIER"/&gt;</xsl:template>
  <xsl:template match="/@rel">&lt;xsl:value-of select="@rel"/&gt;</xsl:template>
  <xsl:template match="/@except">&lt;xsl:value-of select="@except"/&gt;</xsl:template>
  <xsl:template match="/@IDENTIFIER">&lt;xsl:value-of select="@IDENTIFIER"/&gt;</xsl:template>
  <xsl:template match="/@rel">&lt;xsl:value-of select="@rel"/&gt;</xsl:template>
  <xsl:template match="/@except">&lt;xsl:value-of select="@except"/&gt;</xsl:template>
  <xsl:template match="/@IDENTIFIER">&lt;xsl:value-of select="@IDENTIFIER"/&gt;</xsl:template>
  <xsl:template match="/@obj">&lt;xsl:value-of select="@obj"/&gt;</xsl:template>
  <xsl:template match="/@IDENTIFIER">&lt;xsl:value-of select="@IDENTIFIER"/&gt;</xsl:template>
  <xsl:template match="/@bearer">&lt;xsl:value-of select="@bearer"/&gt;</xsl:template>
  <xsl:template match="/@target">&lt;xsl:value-of select="@target"/&gt;</xsl:template>
  <xsl:template match="/@bearer">&lt;xsl:value-of select="@bearer"/&gt;</xsl:template>
  <xsl:template match="/@bearer">&lt;xsl:value-of select="@bearer"/&gt;</xsl:template>
  <xsl:template match="/@bearer">&lt;xsl:value-of select="@bearer"/&gt;</xsl:template>
  <xsl:template match="/@repar">&lt;xsl:value-of select="@repar"/&gt;</xsl:template>
  <xsl:template match="/@has_penalty">&lt;xsl:value-of select="@has_penalty"/&gt;</xsl:template>
  <xsl:template match="/@IDENTIFIER">&lt;xsl:value-of select="@IDENTIFIER"/&gt;</xsl:template>
  <xsl:template match="/@except">&lt;xsl:value-of select="@except"/&gt;</xsl:template>
  <xsl:template match="/@is_except_list_header">&lt;xsl:value-of select="@is_except_list_header"/&gt;</xsl:template>
  <xsl:template match="/@is_except_list_items">&lt;xsl:value-of select="@is_except_list_items"/&gt;</xsl:template>
  <xsl:template match="/@type">&lt;xsl:value-of select="@type"/&gt;</xsl:template>
  <xsl:template match="/@bearer">&lt;xsl:value-of select="@bearer"/&gt;</xsl:template>
  <xsl:template match="/@type">&lt;xsl:value-of select="@type"/&gt;</xsl:template>
  <xsl:template match="/@bearer">&lt;xsl:value-of select="@bearer"/&gt;</xsl:template>
  <xsl:template match="/@type">&lt;xsl:value-of select="@type"/&gt;</xsl:template>
  <xsl:template match="/@IDENTIFIER">&lt;xsl:value-of select="@IDENTIFIER"/&gt;</xsl:template>
  <xsl:template match="/@id">&lt;xsl:value-of select="@id"/&gt;</xsl:template>
  <xsl:template match="/@ref">&lt;xsl:value-of select="@ref"/&gt;</xsl:template>
  <xsl:template match="/@id">&lt;xsl:value-of select="@id"/&gt;</xsl:template>
  <xsl:template match="/@ref">&lt;xsl:value-of select="@ref"/&gt;</xsl:template>
  <xsl:template match="/@id">&lt;xsl:value-of select="@id"/&gt;</xsl:template>
  <xsl:template match="/@ref">&lt;xsl:value-of select="@ref"/&gt;</xsl:template>
  <xsl:template match="/@id">&lt;xsl:value-of select="@id"/&gt;</xsl:template>
</xsl:stylesheet>
