@Repository("qblo001m_01DAO")
public class Qblo001m_01DAO extends EfcAbstractDAO {


	public LnRatRsltVo retrieveUnmbCrdtInrtRt(LnAplcSrchVo lnRatSrchVo) {
		if(log.isDebugEnabled())
			log.debug("=========retrieveUnmbCrdtInrtRt 이자율조회=========");
		
		LnRatRsltVo result = new LnRatRsltVo();
		
		// 이자율
		lnRatSrchVo.setLnRatDcd("0007");	// 융자요율구분코드(0007 이자율)
		Double lnInrt  = select("Qblo001m_01DAO.retrieveUnmbCrdtInrtRt", lnRatSrchVo);
		
		// 3개월전 연체이자율
		lnRatSrchVo.setLnRatDcd("0008");	// 융자요율구분코드(0008 이자연체율(3개월이하))
		Double bfrDlyInrt  = select("Qblo001m_01DAO.retrieveUnmbCrdtInrtRt", lnRatSrchVo);
		
		// 3개월초과 연체이자율
		lnRatSrchVo.setLnRatDcd("0009");	// 융자요율구분코드(0009 이자연체율(3개월초과))
		Double aftrDlyInrt  = select("Qblo001m_01DAO.retrieveUnmbCrdtInrtRt", lnRatSrchVo);
		
		result.setLnInrt(lnInrt);
		result.setBfrDlyInrt(bfrDlyInrt);
		result.setAftrDlyInrt(aftrDlyInrt);
		
		return result;
	}
}