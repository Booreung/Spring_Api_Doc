@Controller
public class LnRpymController extends EfcAbstractController{

    @Resource(name = "lnRpymService")
    private LnRpymService lnRpymService;

    @Resource(name = "lnCntrService")
    private LnCntrService lnCntrService;
    
    @Resource(name = "brpCommService")
    private BrpCommService brpCommService;
    
    @Resource(name = "lnAplcService")
    private LnAplcService lnAplcService;
    
    @Resource(name = "GdsIfrmMngmService")
	private GdsIfrmMngmService gdsIfrmMngmService;
    
    
    @Resource(name = "bumCommService")
    private BumCommService bumCommService;
    
     
    @ScrollPaging
	@RequestMapping(value = "/b/lo/rm/retrieveLnRpymSbjcList.do")
	public ModelAndView retrieveLnRpymSbjcList(HttpServletRequest req, HttpServletResponse res, LnRpymMngmVo input) {

		ModelAndView mav = new ModelAndView("wqView");
		
		try {
			 
			LnRpymMngmVo result = lnRpymService.retrieveLnRpymSbjcList(input);
			
			mav.addObject("result", result);
			EfcSessionUtil.setMessage("EFCCOMN00001", new String[]{"융자상환목록 조회"}); //EFCCOMN00001={0} 작업이 성공적으로 수행되었습니다. 
		} catch (Exception e) {
				// // e.printStackTrace();
				throw new EfcBizException("EFCCOME00001", new String[]{"융자상환목록 조회"}, e); // , e.getCause()); //EFCCOME00001={0} 작업 중 오류가 발생하였습니다. 
		}
		return mav;
	}
}