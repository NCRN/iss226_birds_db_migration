SELECT tbl_Locations.*, tbl_Sites.Site_ID, tbl_Sites.GIS_Location_ID, tbl_Sites.Site_Name, tbl_Sites.Site_Desc, tbl_Sites.Site_Notes, tbl_Sites.Route_Type
FROM tbl_Locations LEFT JOIN tbl_Sites ON tbl_Sites.Site_ID = tbl_Locations.Site_ID;