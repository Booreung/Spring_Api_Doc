
@Service("lnRpymService")
public  class LnRpymServiceImpl extends EfcAbstractService implements LnRpymService {

    @PrivateInfoMethod
    public LnRpymMngmVo retrieveLnRpymSbjcList(LnRpymMngmVo lnRpymMngmVo){

    	LnRpymDscrSrchVo lnRpymDscrSrchVo = lnRpymMngmVo.getLnRpymDscrSrchVo();

    	List<LnRpymDscrRsltVo> LnRpymDscrVoList = qblo102x_01DAO.retrieveLnRpymSbjcList(lnRpymDscrSrchVo);

    	LnRpymMngmVo result = new LnRpymMngmVo();
    	result.setLnRpymDscrRsltVoList(LnRpymDscrVoList);

    	return result;

    }
}