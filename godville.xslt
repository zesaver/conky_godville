<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/">
Герой: <xsl:value-of select="/hero/name"/>
Пол: <xsl:value-of select="/hero/gender"/>
Клан: <xsl:value-of select="/hero/clan"/>
Девиз: <xsl:value-of select="/hero/motto"/>
Характер: <xsl:value-of select="/hero/alignment"/>
Уровень: <xsl:value-of select="/hero/level"/>+<xsl:value-of select="/hero/exp_progress"/>/100
Инвентарь: <xsl:value-of select="/hero/inventory_num"/>/<xsl:value-of select="/hero/inventory_max_num"/>
<xsl:for-each select="/hero/inventory/item">
  {@cnt} * <xsl:apply-templates/>
</xsl:for-each>
Здоровье: <xsl:value-of select="/hero/health"/>/<xsl:value-of select="/hero/max_health"/>
Прана: <xsl:value-of select="/hero/godpower"/>/100
Золотых: <xsl:value-of select="/hero/gold_approx"/>
Последняя запись: <xsl:value-of select="/hero/diary_last"/>
Задание: <xsl:value-of select="/hero/quest_progress"/>/100
  <xsl:value-of select="/hero/quest"/>
</xsl:template>
</xsl:stylesheet>
