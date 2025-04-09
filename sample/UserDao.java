@Repository("qblo001m_01DAO")
public class Qblo001m_01DAO extends EfcAbstractDAO {


	public List<LnRpymDscrRsltVo> retrieveLnRpymSbjcList(LnRpymDscrSrchVo lnRpymDscrSrchVo) {
		if (log.isDebugEnabled())
			log.debug("======================retrieveLnRpymDscrList===================");

		// for nextKey column setting
		CommonUtil.setNextKeyCol(new String[] { "unmbNo", "lnCntrNo", "lnRpymSeq" });

		// for initial nextKey setting
		if (!CommonUtil.isExistNextKey())
			lnRpymDscrSrchVo.setNextKey(" ^ ^0"); // 여러개인 경우에는 ^ 로 구분하여 넣는다. 예) "0^ ^ ..."

		List<LnRpymDscrRsltVo> result = listScroll("Qblo102x_01DAO.retrieveLnRpymSbjcList", lnRpymDscrSrchVo);
		return result;
	}
}