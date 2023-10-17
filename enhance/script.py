import re
import os
from playwright.sync_api import Page
from playwright.sync_api import Playwright, sync_playwright, expect

# <-----------------Change the required setups here----------------->
channelName = "msedge"
speed = 600
timer = 12  # hours

# <---------------Reactor page---------------->
# <---------------Historical Data---------------->
dataSource = "FXView-Demo"
symbol = "USDCHF"
period = "H1"
# <---------------Strategy Properties---------------->
entrylots = "0.01"
oppEntrySignalOption = "2"
stopLossOption = "0"
typeOption = "3"
minPips = "1"
maxPips = "1000"
takeProfitOptions = "0"
tpRangeMin = "2"
tpRangeMax = "1000"
# <---------------Generator Settings---------------->
searchBestOption = "4"
maxEntryOption = "8"
maxExitOption = "4"
runTime = "720"
# <----------------Data Horizon------------------->
maxDataBars = "200000"
startDate = "2018-09-14"
# <------------------------------------------>
collectionCapacity = "300"
accMinNetProfit = "250"
minCountOfTrade = "50"
minSharpeRatio = "0.01"
montCarloMinNetProfit = "50"
montCarloMinCountOfTrade = "50"
minProfitFactor = "1.01"
# ViewPort size setup
vpWidth = 550
vpHeight = 250

#<-------------------Files to change for enhancement-------------------->
PFthreshold = 2
NPthreshold = 30000
maxDrawdownThreshold = 10
SRthreshold = 0.1
#================>
collection = "Strategy Collection 300 EURNZD H1 FXView-Demo; .json"
Path = ""
downloadFolderPath = ""
# <-----------------Change the required setups here----------------->


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False,channel= channelName,slow_mo= speed)
    context = browser.new_context(storage_state="auth.json")
    page = context.new_page()
    page.goto("https://expert-advisor-studio.com/")
    page.get_by_label("Theme").select_option("dark")
    page.wait_for_timeout(3000)

    def RunOrStopReactor(page: Page):
        page.wait_for_selector("#acquisition-link")
        page.click("#acquisition-link")
        
        page.wait_for_selector("#button-start-stop")
        page.click("#button-start-stop")
    
    def initial_setup():
        page.get_by_role("link", name="Tools").click()
        page.get_by_label("Collection capacity").select_option(collectionCapacity)
        page.get_by_role("link", name="Acceptance Criteria").click()
        page.locator("#validation-metrics-base div").filter(has_text=re.compile(r"^Minimum net profit$")).get_by_role("spinbutton").click()
        page.locator("#validation-metrics-base div").filter(has_text=re.compile(r"^Minimum net profit$")).get_by_role("spinbutton").press("Control+a")
        page.locator("#validation-metrics-base div").filter(has_text=re.compile(r"^Minimum net profit$")).get_by_role("spinbutton").fill(accMinNetProfit)
        page.locator("div").filter(has_text=re.compile(r"^Minimum count of trades$")).get_by_role("spinbutton").click()
        page.locator("div").filter(has_text=re.compile(r"^Minimum count of trades$")).get_by_role("spinbutton").press("Control+a")
        page.locator("div").filter(has_text=re.compile(r"^Minimum count of trades$")).get_by_role("spinbutton").fill(minCountOfTrade)
        page.locator("#validation-metrics-base").get_by_role("button", name="+ Add acceptance criteria").click()
        page.get_by_role("link", name="Minimum Sharpe ratio").click()
        page.locator("div").filter(has_text=re.compile(r"^Minimum Sharpe ratio$")).get_by_role("spinbutton").click()
        page.locator("div").filter(has_text=re.compile(r"^Minimum Sharpe ratio$")).get_by_role("spinbutton").press("Control+a")
        page.locator("div").filter(has_text=re.compile(r"^Minimum Sharpe ratio$")).get_by_role("spinbutton").fill(minSharpeRatio)
        page.get_by_role("link", name="Available Indicators").click()
        page.locator("#toggle-entries").click()
        page.locator("#toggle-entries").click()
        page.locator("#toggle-exits").click()
        page.locator("#toggle-exits").click()
        page.get_by_role("row", name="Do not Exit").get_by_role("checkbox").uncheck()
        page.get_by_role("row", name="Exit Time").get_by_role("checkbox").uncheck()
        page.get_by_role("link", name="Data").click()
        page.get_by_role("link", name="Data Horizon").click()
        page.get_by_label("Maximum data bars").click()
        page.get_by_label("Maximum data bars").press("Control+a")
        page.get_by_label("Maximum data bars").fill(maxDataBars)
        page.get_by_label("Start date", exact=True).press("Control+a")
        page.get_by_label("Start date", exact=True).fill(startDate)
        page.get_by_label("Use start date limit").check()
        page.get_by_role("link", name="Strategy ID -").click()
        page.get_by_role("link", name="Monte Carlo").click()
        page.get_by_label("Randomize history data").uncheck()
        page.get_by_label("Randomize spread").uncheck()
        page.get_by_label("Randomize slippage").uncheck()
        page.get_by_label("Randomly skip position entry").uncheck()
        page.get_by_label("Randomly skip position exit").uncheck()
        page.get_by_label("Randomize indicator parameters").check()
        page.get_by_label("Randomize backtest starting bar").check()
        page.get_by_role("link", name="Validation").click()
        page.locator("div").filter(has_text=re.compile(r"^Minimum net profit$")).get_by_role("spinbutton").click()
        page.locator("div").filter(has_text=re.compile(r"^Minimum net profit$")).get_by_role("spinbutton").press("Control+a")
        page.locator("div").filter(has_text=re.compile(r"^Minimum net profit$")).get_by_role("spinbutton").fill(montCarloMinNetProfit)
        page.locator("div").filter(has_text=re.compile(r"^Minimum count of trades$")).get_by_role("spinbutton").click()
        page.locator("div").filter(has_text=re.compile(r"^Minimum count of trades$")).get_by_role("spinbutton").press("Control+a")
        page.locator("div").filter(has_text=re.compile(r"^Minimum count of trades$")).get_by_role("spinbutton").fill(montCarloMinCountOfTrade)
        page.get_by_role("button", name="+ Add validation criteria").click()
        page.get_by_role("link", name="Minimum profit factor").click()
        page.locator("div").filter(has_text=re.compile(r"^Minimum profit factor$")).get_by_role("spinbutton").click()
        page.locator("div").filter(has_text=re.compile(r"^Minimum profit factor$")).get_by_role("spinbutton").press("Control+a")
        page.locator("div").filter(has_text=re.compile(r"^Minimum profit factor$")).get_by_role("spinbutton").fill(minProfitFactor)
        page.get_by_role("link", name="Open the Generator, the Reactor, or the Validator").click()
        page.get_by_role("link", name="Reactor", exact=True).click()

        page.get_by_label("Data source").select_option(dataSource)
        page.get_by_label("Symbol").select_option(symbol)
        page.get_by_label("Period").select_option(period)
        
        page.locator("div").filter(has_text=re.compile(r"^2\. Strategy properties$")).click()
        page.get_by_label("Entry lots").click()
        page.get_by_label("Entry lots").press("Control+a")
        page.get_by_label("Entry lots").fill(entrylots)
        page.get_by_label("Opposite entry signal").select_option(oppEntrySignalOption)
        page.get_by_label("Stop Loss", exact=True).select_option(stopLossOption)
        page.get_by_label("Type").select_option(typeOption)
        page.get_by_role("spinbutton", name="Min (pips)").click()
        page.get_by_role("spinbutton", name="Min (pips)").press("Control+a")
        page.get_by_role("spinbutton", name="Min (pips)").fill(minPips)
        page.get_by_role("spinbutton", name="Max (pips)").click()
        page.get_by_role("spinbutton", name="Max (pips)").press("Control+a")
        page.get_by_role("spinbutton", name="Max (pips)").fill(maxPips)
        page.locator("div").filter(has_text=re.compile(r"^3\. Generator settings$")).click()
        page.locator("#search-best").select_option(searchBestOption)
        page.get_by_label("Max entry indicators").select_option(maxEntryOption)
        page.get_by_label("Max exit indicators").select_option(maxExitOption)
        page.get_by_label("Generate strategies with\nPreset Indicators").uncheck()
        page.get_by_label("Working minutes").click()
        page.get_by_label("Working minutes").press("Control+a")
        page.get_by_label("Working minutes").fill(runTime)
        page.get_by_role("link", name="Open the Generator, the Reactor, or the Validator").click()
        page.get_by_label("", exact=True).get_by_role("link", name="Reactor").click()
        page.locator("div").filter(has_text=re.compile(r"^1\. Historical data$")).click()
        
        page.get_by_role('button',name='Confirm').click()
        
        page.wait_for_timeout(10000)
        # page.wait_for_selector('#acquisition-link')
        # page.click('#acquisition-link')

        RunOrStopReactor()
        page.set_viewport_size({"width": 550, "height": 250})
    
    def analyze_backtest_results3(page:Page, NP_threshold, max_drawdown_threshold, SR_threshold, PF_threshold):
        # Go to portfolio
        page.wait_for_selector('#eas-navbar-portfolio-link')
        page.click('#eas-navbar-portfolio-link')

        page.wait_for_selector('#backtest-output-table')

        def evaluate_threshold(value, threshold):
            return value > threshold

        def get_value_and_threshold(selector, threshold):
            element =  page.locator(selector)
            value_text =  element.text_content()
            value = float(value_text.split(' ')[0].replace(',', ''))
            return {'value': value, 'meets_threshold': evaluate_threshold(value, threshold)}

        net_profit =  get_value_and_threshold('#backtest-profit', NP_threshold)
        max_drawdown =  get_value_and_threshold('#backtest-drawdown-percent', max_drawdown_threshold)
        sharp_ratio =  get_value_and_threshold('#backtest-sharpe-ratio', SR_threshold)
        profit_factor =  get_value_and_threshold('#backtest-profit-factor', PF_threshold)

        print(f"Net Profit: {net_profit['value']} | Max Drawdown: {max_drawdown['value']}% | Sharp Ratio: {sharp_ratio['value']} | Profit Factor: {profit_factor['value']}")

        return {
            'netProfit': net_profit['value'],
            'maxDrawdown': max_drawdown['value'],
            'sharpRatio': sharp_ratio['value'],
            'profitFactor': profit_factor['value'],
            'isProfitFactorGreater': profit_factor['meets_threshold'],
            'isNetProfitGreater': net_profit['meets_threshold'],
            'isMaxDrawdownLess': not max_drawdown['meets_threshold'],
            'isSharpRatioGreater': sharp_ratio['meets_threshold']
        }


    def clear_portfolio(page: Page):
        page.wait_for_selector("#eas-navbar-portfolio-link")
        page.click("#eas-navbar-portfolio-link")

        # Now, Delete the portfolio and collection
        page.wait_for_selector("#remove-all-button")
        page.click("#remove-all-button")
        print("Portfolio deleted")

    def clear_collection(page: Page):
        # Go to collection page
        page.wait_for_selector("#eas-navbar-collection-link")
        page.click("#eas-navbar-collection-link")

        # Clear collections
        page.wait_for_selector("#remove-all-button")
        page.click("#remove-all-button")
        print("Collection Deleted")
    
    def download_files(page: Page, download_folder_path, collection_download_path):
        # Export the portfolio and download the unfiltered collection
        page.wait_for_selector("#portfolio-toolbar-export")
        page.click("#portfolio-toolbar-export")
        page.wait_for_selector("#export-portfolio-expert-mt5")

        # Wait for download to start
        download = page.wait_for_event("download")
        page.click("#export-portfolio-expert-mt5")

        download_path = os.path.join(download_folder_path, download.suggested_filename())
        download.save_as(download_path)
        print("Download saved to:", download_path)

        page.wait_for_selector("#eas-navbar-collection-link")
        page.click("#eas-navbar-collection-link")
        page.wait_for_selector("#download-collection")
        page.click("#download-collection")

        collection_download = page.wait_for_event("download")
        page.locator("a[aria-label='Collection']").click()

        collection_download.save_as(collection_download_path)
        print("Collected strategies saved to:", collection_download_path)
        print("Script1 download finished")

    def upload_collection(page: Page, collection_download_path):
        page.wait_for_selector("#eas-navbar-collection-link")
        page.click("#eas-navbar-collection-link")
        input_element = page.locator("input[type='file']")
        input_element.set_input_files(collection_download_path)

    def get_collection_number(page: Page):
        # Get the value from collection notification
        produced_strategies = page.eval_on_selector('#eas-collection-notification', 'element => element.textContent.trim()')

        produced_strategies = int(produced_strategies)  # Convert the result to an integer

        if produced_strategies <= 30:
            print("No. of strategies produced:", produced_strategies)
            # Call strategyOne() here if needed
        elif 30 < produced_strategies <= 150:
            print("No. of strategies produced:", produced_strategies)
        elif 150 < produced_strategies <= 240:
            print("No. of strategies produced:", produced_strategies)
            # Call strategyThree() here if needed



#########################################

    def update_sharpe_ratio(page: Page, current_sr_threshold):
        page.wait_for_selector('#eas-navbar-collection-link')
        page.click('#eas-navbar-collection-link')
        page.locator('div').filter(has_text=re.compile(r'^Minimum Sharpe ratio$')).get_by_role('spinbutton').fill(current_sr_threshold)
        page.click('#eas-main-container')

    def change_sharpe_ratio_acceptance_criteria(sharpe_ratio, page:Page):
        page.wait_for_selector('#eas-navbar-tools-link')
        page.click('#eas-navbar-tools-link')
        page.wait_for_selector('#eas-navbar-acceptance-criteria-link')
        page.click('#eas-navbar-acceptance-criteria-link')

        page.locator('div').filter(has_text=re.compile(r'^Minimum Sharpe ratio$')).get_by_role('spinbutton').click()
        page.locator('div').filter(has_text=re.compile(r'^Minimum Sharpe ratio$')).get_by_role('spinbutton').press('Control+A')
        page.locator('div').filter(has_text=re.compile(r'^Minimum Sharpe ratio$')).get_by_role('spinbutton').fill(str(sharpe_ratio))

    def activate_performance_filter(page:Page):
        page.wait_for_selector('#eas-navbar-collection-link')
        page.click('#eas-navbar-collection-link')

        page.select_option('label=Sort collection by', 'SharpeRatio')
        page.check('label=Use performance filters.')
        page.locator('div').filter(has_text=re.compile(r'^Minimum net profit$')).locator('i').click()
        page.click('button:has-text("+ Add validation criteria")')
        page.click('a:has-text("Minimum Sharpe ratio")')
        page.click('input:has-role("spinbutton")')
        page.press('input:has-role("spinbutton")', 'Control+A')
        page.fill('input:has-role("spinbutton")', '0.07')
        page.click('#eas-main-container')

    def check_performance_filter(page:Page):
        page.wait_for_selector('#eas-navbar-collection-link')
        page.click('#eas-navbar-collection-link')

        page.check('label=Use performance filters.')

    def uncheck_performance_filter(page:Page):
        page.wait_for_selector('#eas-navbar-collection-link')
        page.click('#eas-navbar-collection-link')

        page.uncheck('label=Use performance filters.')

#########################################

    def strategy_one(page: Page):
        # Change the stop loss and take profit
        page.locator("div").filter(has_text="^2\. Strategy properties$").click()
        page.get_by_label("Stop Loss", exact=True).select_option("1")
        page.get_by_label("Take Profit", exact=True).select_option("1")
        RunOrStopReactor(page)


    def strategy_three(page: Page):
        PFthreshold = 2
        NPthreshold = 30000
        SRthreshold = 0.1
        maxDrawdownThreshold = 10
        initialSRthreshold = 0.07
        maxSRthreshold = 0.5
        SRincrement = 0.02

        currentSRthreshold = initialSRthreshold
        isCriteriaMet = False

        analysisResults = analyze_backtest_results3(page, NPthreshold, maxDrawdownThreshold, SRthreshold, PFthreshold)

        if analysisResults['isMaxDrawdownLess'] and analysisResults['isProfitFactorGreater'] and analysisResults['isSharpRatioGreater']:
            print("All three conditions met")
            analysisResults = analyze_backtest_results3(page, NPthreshold, maxDrawdownThreshold, SRthreshold, PFthreshold)
            print(f"Analysis results: {analysisResults}")
            download_files()
            clear_collection()
            clear_portfolio()
        else:
            print("Inside Else")
            activate_performance_filter()
            while analysisResults['maxDrawdown'] >= 10.0 and analysisResults['sharpRatio'] < 0.1:
                print("Increasing sharpe ratio.....")
                # Change sharp ratio
                currentSRthreshold = currentSRthreshold + SRincrement
                update_sharpe_ratio(currentSRthreshold)
                analysisResults = analyze_backtest_results3(page, NPthreshold, maxDrawdownThreshold, SRthreshold, PFthreshold)
                print(analysisResults)

            analysisResults = analyze_backtest_results3(page, NPthreshold, maxDrawdownThreshold, SRthreshold, PFthreshold)

            if not analysisResults['isProfitFactorGreater']:
                print("Profit factor is greater downloading files.")
                download_files()
                uncheck_performance_filter()
                download_files()
            else:
                print("Profit factor is smaller re-running reactor.")
                files = download_files()
                clear_portfolio()
                clear_collection()
                print(files['collectionDownloadPath'])
                upload_collection(files['collectionDownloadPath'])

                # Change sharp ratio in acceptance criteria
                change_sharp_ratio_acceptance_criteria(currentSRthreshold - 0.01)
                RunOrStopReactor()

    def strategy_four(page: Page):
        PFthreshold = 2
        NPthreshold = 30000
        SRthreshold = 0.1
        maxDrawdownThreshold = 10
        initialSRthreshold = 0.15
        maxSRthreshold = 0.5
        SRincrement = 0.05

        currentSRthreshold = initialSRthreshold
        isCriteriaMet = False

        analysisResults = analyze_backtest_results3(page, NPthreshold, maxDrawdownThreshold, SRthreshold, PFthreshold)

        if analysisResults['isMaxDrawdownLess'] and analysisResults['isProfitFactorGreater'] and analysisResults['isSharpRatioGreater']:
            activate_performance_filter()
            strategies = get_strategies()
            while strategies < 90:
                currentSRthreshold = currentSRthreshold + SRincrement
                update_sharpe_ratio(currentSRthreshold)
                strategies = get_strategies()

            download_files()
            clear_collection()
            clear_portfolio()
            upload_collection()
            change_sharpe_ratio_acceptance_criteria(currentSRthreshold)
            RunOrStopReactor()




    initial_setup()
    page.wait_for_timeout(1000 * 60 * 60 * timer) 



    # page.get_by_role("button", name="Start").click()
    # page.get_by_role("button", name="Stop").click()

    # ---------------------
    # context.close()
    # browser.close()




# Example usage:
# strategy_one(page)

# Example usage:
# download_folder_path = "C:/Users/FCTwin1001/Downloads/automation_downloads/USDCHF/"
# collection_download_path = os.path.join(download_folder_path, "collection_file.zip")
# download_files(page, download_folder_path, collection_download_path)
# upload_collection(page, collection_download_path)


with sync_playwright() as playwright:
    run(playwright)
