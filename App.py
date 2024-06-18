import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from streamlit_option_menu import option_menu
from src.streamlit_extras.metric_cards import style_metric_cards

class DashboardApp:
    _option_menu_counter = 0
    def __init__(self):
        st.set_page_config(page_title="Dashboard", page_icon="📊", layout="wide")

        hide_st_style = """<style> #MainMenu {visibility: true;} footer {visibility: hidden;} </style>"""
        st.markdown(hide_st_style, unsafe_allow_html=True)
        #st.markdown('<footer id="YourNameInFooter"><p>Amit Tiwari</p></footer>', unsafe_allow_html=True)
        st.subheader("🔔  Performance Metrics")
        st.markdown("##")
        
        self.user_db = {
            "06423": "password123",
            "00030": "password123",
            "06623":"password1234",
            "06788":"password1234",
            "00160":"password1234",
            "01085":"password1234",
            "00001":"password1234"
        }
        #self.theme_plotly = "Light"  # None or streamlit

    def authenticate_user(self, username, password):
        if username in self.user_db and self.user_db[username] == password:
            return True
        return False

    def option_menu_fun(self):
        option_menu_key = f"option_menu_{DashboardApp._option_menu_counter}"
        DashboardApp._option_menu_counter += 1
        #sorted_options = ["Home", "Outstanding", "New / Closed Business",  "Billing Summary"]#sorted(["Home", "Outstanding", "New / Closed Business", "PV Details", "Billing Summary"])
        sorted_options = ["Home", "Outstanding"]
        selected=option_menu(
            key=option_menu_key,
            menu_title=None,
            options=sorted_options,#["Home","Outstanding","Option1","Opction2","Opction3"],
            icons=["house", "eye", "eye", "eye"],
            menu_icon="cast",
            default_index=0,
            orientation="horizontal"
        )
        if selected=="Home":
            app.main()
            #pass

        if selected == "Outstanding":
            #pass
            app.outstanding()

        if selected == "Billing Summary":
            pass
            #app.billing_summary()
        
        if selected == "New / Closed Business":
            pass
            #self.New_Closed_Business()

    def login(self):
        
        log1, log2, log3 = st.columns(3, gap='large')
        with log2:
            st.title("DASHBOARD LOGIN")
            username_key = "username_input"
            password_key = "password_input_"
            username = st.text_input("Username", key=username_key)
            password = st.text_input("Password", type="password", key=password_key)
            if st.button("Login"):
                if self.authenticate_user(username, password):
                    st.session_state['loggedIn'] = True
                    st.session_state['username'] = username
                    st.success("Logged in Successfully!")
                    #self.option_menu_fun()
                    return True, username
                else:
                    st.session_state['loggedIn'] = False
                    st.error("Login failed. Please check your credentials.")
            return False, None


    def mainMenu(self):
        if 'loggedIn' not in st.session_state:
            st.session_state['loggedIn']=False

        if st.session_state['loggedIn'] == True:
            if st.session_state['username'] == '06423':
                self.cad_id = 2
                self.name = 'Mr. ADITYA AMARJEET SINGH'
            elif st.session_state['username'] == '00030':
                self.cad_id = 5
                self.name = 'Mrs. GITA VISHAL SINGH'

            elif st.session_state['username'] == '01085':
                self.cad_id = 7
                self.name = 'Mr. Anttesh Rajesh Singh'

            elif st.session_state['username'] == '00160':
                self.cad_id = 4
                self.name = 'Mr. Santosh R Singh'

            st.sidebar.markdown('<center><p><h1 style="color: black; font-family: Helvetica, sans-serif;">BOMBAY INTEGRATED SECURITY (INDIA) LTD</h1></p></center>', unsafe_allow_html=True)
            #st.logo("data/logo1.png", link=None, icon_image="data/logo1.png", caption="BOMBAY INTEGRATED SECURITY (INDIA) LTD")
            st.sidebar.image("data/logo1.png", caption="")
            if st.session_state['username'] == '00160':
                st.sidebar.markdown(f'<center><p><h2 style="color: black; font-family: Helvetica, sans-serif;">Honorable CMD <br>  {self.name}</h2></p></center>',unsafe_allow_html=True)
            else:
                st.sidebar.markdown(f'<center><p><h2 style="color: black; font-family: Helvetica, sans-serif;">Honorable Director <br>  {self.name}</h2></p></center>',unsafe_allow_html=True)
    
    def main(self):
        if 'loggedIn' not in st.session_state:
            st.session_state['loggedIn'] = False

        if st.session_state['loggedIn'] == True:
            #conn = self.create_connection()
            self.mainMenu()
            
            #filtered_df = pd.read_excel('data\invoicedata.xlsx')
            filtered_df=pd.read_excel('http://203.187.225.154/BISMARVELNEWTEST/invoicedata.xlsx')
            df = filtered_df[filtered_df['CadId'] == 2]

            options = ['Monthly', 'Yearly']
            report_type = st.sidebar.radio("Select Report Type", options)

            sorted_year = sorted(df["InvoiceYear"].unique())
            invoiceYear = st.sidebar.selectbox(
                "Select Year",
                options=sorted_year[::-1],
                #options=df["InvoiceYear"].unique(),
                #default=df["InvoiceYear"].unique(),
            )

            if report_type == 'Yearly':
                invoiceMonth = st.sidebar.multiselect(
                    "Select Month",
                    options=df["InvoiceMonth"].unique(),
                    default=df["InvoiceMonth"].unique(),
                )
            else:
                sorted_months = sorted(df["InvoiceMonth"].unique())
                invoiceMonth = st.sidebar.selectbox(
                    "Select Month",
                    options =sorted_months, #df["InvoiceMonth"].unique(),#[::-1],
                    #default=df["InvoiceMonth"].unique()[::-1],
                )

                if invoiceMonth == 'January':
                    monthNumber=1
                elif invoiceMonth == 'February':
                    monthNumber=2
                elif invoiceMonth == 'March':
                    monthNumber=3
                elif invoiceMonth == 'April':
                    monthNumber=4
                elif invoiceMonth == 'May':
                    monthNumber=5
                elif invoiceMonth =='June':
                    monthNumber=6
                elif invoiceMonth == 'July':
                    monthNumber=7
                elif invoiceMonth == 'August':
                    monthNumber=8
                elif invoiceMonth == 'September':
                    monthNumber=9
                elif invoiceMonth == 'October':
                    monthNumber=10
                elif invoiceMonth == 'November':
                    monthNumber=11
                elif invoiceMonth == 'December':
                    monthNumber=12

            st.sidebar.header("Please filter")
            brLocName = st.sidebar.multiselect(
                "Select Branch",
                options=df["BrLocName"].unique(),
                default=df["BrLocName"].unique(),
            )

            df_selection = df.query("BrLocName == @brLocName & InvoiceYear == @invoiceYear & InvoiceMonth == @invoiceMonth")

            total_invoice_amount = df_selection['InvoiceAmount'].sum()

            invoice_count = df_selection['InvoiceNo'].count()

            if report_type == 'Monthly':
                df = df[df['InvoiceYear']==invoiceYear]
                count_of_invoices = len(df.loc[df["Invoice_Month"] == int(monthNumber - 1)])
                diff = (invoice_count - count_of_invoices)
                previous_month_Amount = df[df["Invoice_Month"] == int(monthNumber - 1)]["InvoiceAmount"].sum()
                Amount_Diff = (total_invoice_amount - previous_month_Amount)

                with open('style.css')as f:
                    st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)


                def  cards_():

                    total1, total2, total3, total4,total5 = st.columns(5)

                    total1.metric(label="Invoice Count Summary",label_visibility="visible", value=f"🧾 {invoice_count:,.0f}")
                        

                    total2.metric(label="Invoice Quantity Variations", value=f"🖆 {diff:,.0f}")
                    
                    total3.metric(label="Total Invoice Value", value=f"💰 {total_invoice_amount:,.0f}")

                    if Amount_Diff < 0:
                        total4.metric(label="Variation in Total", value=f"🔴 {Amount_Diff:,.0f}")
                    else:
                        total4.metric(label="Variation in Total", value=f"🟢 {Amount_Diff:,.0f}")

                    total_arr_amount = df_selection[df_selection["InvType"] == 1]["InvoiceAmount"].sum()
                    total5.metric(label="Total Arrer Amount", value=f"{total_arr_amount:,.0f}")
                    style_metric_cards()

                card=st.container()
                with card:
                    cards_()

                stp =st.container()
                
                #right, center = st.columns(2)
                filtered_df = df[df['InvoiceMonth'] == invoiceMonth]

                filtered_df2 = df[df['Invoice_Month'] == monthNumber - 1]

                #st.write(filtered_df2.head(10))

                previous_month = filtered_df2.groupby(by=["BrLocName"])["InvoiceAmount"].sum().reset_index()

                investment_state1 = filtered_df.groupby(by=["BrLocName"])["InvoiceAmount"].sum().reset_index()
                #custom_month_order1 = ['BrLocName']
                #st.write(investment_state1.head(10))
                #st.write(previous_month.head(10))
                merged_df = pd.merge(previous_month, investment_state1, on="BrLocName", suffixes=('_previous_month', '_investment_selected_month'))
                merged_df["diff_amount"]= merged_df["InvoiceAmount_investment_selected_month"] - merged_df["InvoiceAmount_previous_month"]
                
                with stp:
                    col2,col3 = st.columns(2)
                    with col3:

                        merged_df = merged_df.rename(columns={
                            "BrLocName": "Branch",
                            "InvoiceAmount_previous_month": "LastMonth",
                            "InvoiceAmount_investment_selected_month": "CurrentMonth",
                            "diff_amount": "Difference",
                        })
                        

                        # Convert DataFrame to HTML with white background
                        html_table = (
                            merged_df.style
                            .format("{:.0f}", subset=["LastMonth", "CurrentMonth", "Difference"])
                            .bar(subset=["Difference"], align="mid", color=['#d65f5f', '#5fba7d'])
                            .highlight_max(subset=["Difference"], color="#5fba7d")
                            .highlight_min(subset=["Difference"], color="#d65f5f")
                            .set_table_styles([
                                {"selector": "thead th", "props": [("font-weight", "bold"), ("text-align", "center"), ("background-color", "white")]},
                                {"selector": "tbody td", "props": [("text-align", "center"), ("background-color", "white")]}
                            ])
                        ).to_html()

                        # Display HTML table in Streamlit
                        st.markdown(html_table, unsafe_allow_html=True)

                investment_state1 = investment_state1.sort_values(by="InvoiceAmount", ascending=False)

                fig_state = px.bar(
                    investment_state1,
                    x="BrLocName",
                    y="InvoiceAmount",
                    title="<b>Amount Trends by Month </b>",
                    labels='InvoiceAmount',
                    text='InvoiceAmount',
                    #color_discrete_sequence=["#b34d4d"],
                    color="BrLocName",
                    #color_discrete_sequence=px.colors.qualitative.Set2,
                    template="plotly_white",
                    
                )

                fig_state.update_traces(
                    texttemplate='%{text:.2s}',
                    textposition='outside',
                    )

                fig_state.update_layout(
                    xaxis=dict(categoryorder="array", tickmode="array"),
                    #plot_bgcolor="#777575",
                    font=dict(family="Arial", size=14, color="RebeccaPurple"), 
                    funnelmode="overlay",
                    uniformtext_minsize=6, 
                    #uniformtext_mode='hide'
                    
                    yaxis=dict(showgrid=False)
                    
                ) 
                #fig_state.update_traces(textfont=dict(color='blue', size=14, family='Arial', weight='bold'))  # Customize font style
                
                col2.plotly_chart(fig_state, use_container_width=True) 

                cont =st.container()
                with cont:
                    cont1,cont2 =st.columns(2)
                    with cont2:
                        colors = px.colors.qualitative.Set1_r
                        slice_to_cut = 0

                        # Create a pie chart with additional styling
                        fig = px.pie(
                            df_selection,
                            values='InvoiceAmount',
                            names='BrLocName',
                            title='Branch-wise Performance',
                            color_discrete_sequence=colors,  # Set custom colors
                            hole=0.3,
                        )
                        fig.update_layout(
                            legend_title="Branch",
                            legend_y=0.9,
                            title_x=0.5,  # Center the title
                            font=dict(family="Arial", size=14, color="RebeccaPurple"),  # Customize font
                            margin=dict(l=0, r=0, b=0, t=30),  # Adjust margin for better spacing
                            #paper_bgcolor="lightgray",  # Set background color
                            #plot_bgcolor="white",  # Set plot area color
                        )
                        fig.update_traces(
                            textinfo='percent+label',
                            textposition='inside',
                            hoverinfo='label+percent+name',  # Show additional information on hover
                            marker=dict(line=dict(color='white', width=2)),  # Add white border for better visibility
                            pull=[0.2 if i == slice_to_cut else 0 for i in range(len(df_selection))]
                        )

                        # Display the chart in Streamlit app
                        st.plotly_chart(fig, use_container_width=True, theme="streamlit")
                
                    with cont1:
                        top10=df[df['Invoice_Month'] == monthNumber]
                        top_10_customers = top10.sort_values(by='InvoiceAmount', ascending=False).head(10)

                        #st.dataframe(top_10_customers)

                        fig_state = px.bar(
                            top_10_customers,
                            x="InvoiceAmount",
                            y="CustName",
                            orientation="h",
                            title="<b>Top Clients  </b>",
                            labels='InvoiceAmount',
                            text='InvoiceAmount',
                            #color_discrete_sequence=["#b34d4d"],
                            color="CustName",
                            
                            #color_discrete_sequence=px.colors.qualitative.Set2,
                            template="plotly_white",
                            
                        )

                        fig_state.update_traces(
                            texttemplate='%{text:.2s}',
                            textposition='outside',
                        
                        )

                        fig_state.update_layout(
                            xaxis=dict(categoryorder="array", tickmode="array"),
                            #plot_bgcolor="#777575",
                            font=dict(family="Arial", size=14, color="RebeccaPurple"), 
                            funnelmode="overlay",
                            uniformtext_minsize=6, 
                            #uniformtext_mode='hide'
                            showlegend=False,
                            yaxis=dict(showgrid=False)
                            
                        ) 
                #fig_state.update_traces(textfont=dict(color='blue', size=14, family='Arial', weight='bold'))  # Customize font style
                
                        cont1.plotly_chart(fig_state, use_container_width=True) 




            else:
                with open('style.css')as f:
                    st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
                total1, total3 = st.columns(2, gap='large')
                with total1:
                    #st.info('Invoice Count Summary', icon="📌")
                    st.metric(label="Invoice Count Summary", value=f"🧾 {invoice_count:,.0f}")

                with total3:
                    #st.info('Total Invoice Value', icon="📌")
                    st.metric(label="Total Invoice Value", value=f"💰 {total_invoice_amount:,.0f}")

                st.markdown("---")
                with open('style.css')as f:
                        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

            if report_type == 'Yearly':
                #top_cust = df[df['InvoiceMonth']==invoiceMonth]
                customer_total_invoices = df_selection.groupby("CustName")["InvoiceAmount"].sum()
                sorted_customers = customer_total_invoices.sort_values(ascending=False)
                top_10_customers = sorted_customers.head(10)
                top_10_customers_df = pd.DataFrame({
                    "Customer Identification": top_10_customers.index,
                    "Invoice Sum Summary": top_10_customers.values,
                    "color": ["#1E90FF", "#0083B8", "#00FF00", "#FF5733", "#FFD700", "#FF1493", "#8A2BE2", "#FFA07A", "#FF6347", "#40E0D0"]
                })
            
                fig_investment = px.bar(
                    top_10_customers_df,
                    x="Invoice Sum Summary",
                    y="Customer Identification",
                    orientation="h",
                    title="<b> Top 10 Invoice Clients </b>",
                    color="color",
                    template="plotly_white",
                    labels={"Invoice Sum Summary": "Total Invoice Amount", "Customer Identification": "Customer ID"},
                    
                )

                fig_investment.update_layout(
                    plot_bgcolor="rgba(0,0,0,0)",
                    showlegend=False,
                    xaxis=dict(showgrid=False),
                    font=dict(family="Arial", size=12, color="RebeccaPurple"),
                    hovermode="closest",
                    hoverlabel=dict(bgcolor="black", font_size=12, font_family="Arial"),
                )

            #left,right, center = st.columns(3)
            if report_type == 'Yearly':
                left, right, center = st.columns(3)

                investment_state = df.groupby(by=["InvoiceMonth"])["InvoiceAmount"].sum().reset_index()
                custom_month_order = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

                fig_state = px.scatter(
                    investment_state,
                    x="InvoiceMonth",
                    y="InvoiceAmount",
                    title="<b>Amount Trends by Month </b>",
                    size="InvoiceAmount",
                    color="InvoiceAmount",
                    color_discrete_sequence=px.colors.qualitative.Set1,
                    template="plotly_white",
                )

                fig_state.update_layout(
                    xaxis=dict(categoryorder="array", tickmode="array", categoryarray=custom_month_order),
                    plot_bgcolor="rgba(0,0,0,0)",
                    yaxis=dict(showgrid=False)
                ) 
                left.plotly_chart(fig_state, use_container_width=True) 

                with right:
                    st.plotly_chart(fig_investment, use_container_width=True)
                #pass

                with center:
                    #fig = px.pie(df_selection, values='InvoiceAmount', names='BrLocName', title='Branch-wise Performance')
                    #fig.update_layout(legend_title="Branch", legend_y=0.9)
                    #fig.update_traces(textinfo='percent+label', textposition='inside')
                    #st.plotly_chart(fig, use_container_width=True, theme=self.theme_plotly)

                    colors = px.colors.qualitative.Set1_r
                    slice_to_cut = 0

                    # Create a pie chart with additional styling
                    fig = px.pie(
                        df_selection,
                        values='InvoiceAmount',
                        names='BrLocName',
                        title='Branch-wise Performance',
                        color_discrete_sequence=colors,  # Set custom colors
                        hole=0.3,
                    )
                    fig.update_layout(
                        legend_title="Branch",
                        legend_y=0.9,
                        title_x=0.5,  # Center the title
                        font=dict(family="Arial", size=14, color="RebeccaPurple"),  # Customize font
                        margin=dict(l=0, r=0, b=0, t=30),  # Adjust margin for better spacing
                        #paper_bgcolor="lightgray",  # Set background color
                        #plot_bgcolor="white",  # Set plot area color
                    )
                    fig.update_traces(
                        textinfo='percent+label',
                        textposition='inside',
                        hoverinfo='label+percent+name',  # Show additional information on hover
                        marker=dict(line=dict(color='white', width=2)),  # Add white border for better visibility
                        pull=[0.2 if i == slice_to_cut else 0 for i in range(len(df_selection))]
                    )

                    # Display the chart in Streamlit app
                    st.plotly_chart(fig, use_container_width=True, theme="streamlit")



        else:
            self.login()

    def outstanding(self):
        if 'loggedIn' not in st.session_state:
            st.session_state['loggedIn']=False

        if st.session_state['loggedIn'] == True:
            #conn = self.create_connection()
            self.mainMenu()
            cadid=self.cad_id
            #df=pd.read_excel('data\outstanding.xlsx')
            df=pd.read_excel('http://203.187.225.154/BISMARVELNEWTEST/outstanding.xlsx')
            df_out = df[df['CadId'] == 2]
            #df_out = self.load_data(conn,cadid,query)
            brLocName = st.sidebar.multiselect("Select Branch",options=df_out['BrLocName'].unique(),default=df_out['BrLocName'].unique())
            filtered_df = df_out[df_out['BrLocName'].isin(brLocName)]
            # Key Metrics Section
            st.header('Key Performance Indicators (KPIs)')
            total_invoices = df_out['InvoiceAmount'].count()
            total_paid = df_out['PaidAmount'].sum()
            total_balance = df_out['BalAmount'].sum()

            def  out_cards_():

                    total1, total2, total3 = st.columns(3)

                    total1.metric(label="Total Invoices",label_visibility="visible", value=f"🧾 {total_invoices:,.0f}")
                        

                    total2.metric(label="Total Paid", value=f"🖆 {total_paid:,.0f}")
                    
                    total3.metric(label="Total Balance", value=f"💰 {total_balance:,.0f}")

                    #if Amount_Diff < 0:
                        #total4.metric(label="Variation in Total", value=f"🔴 {Amount_Diff:,.0f}")
                    #else:
                        #total4.metric(label="Variation in Total", value=f"🟢 {Amount_Diff:,.0f}")

                    #total_arr_amount = df_selection[df_selection["InvType"] == 1]["InvoiceAmount"].sum()
                    #total5.metric(label="Total Arrer Amount", value=f"{total_arr_amount:,.0f}")
                    style_metric_cards()

            out_card=st.container()
            with out_card:
                out_cards_()
            col1,col2 = st.columns(2)
            with open('style.css')as f:
                    st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
            with col1:
                # Location-wise Analysis
                st.header('Location-wise Analysis')
                location_df = df_out.groupby('BrLocName').agg({'InvoiceAmount': 'sum', 'PaidAmount': 'sum', 'BalAmount': 'sum'}).reset_index()

                # Bar Chart: Amounts by Location with Lines
                fig_bar_location = px.bar(location_df, x='BrLocName', y=['InvoiceAmount', 'PaidAmount', 'BalAmount'],
                                        title='Amounts by Location', labels={'value': 'Amount', 'variable': 'Type'},
                                        barmode='group')

                # Add line traces for 'PaidAmount', 'BalAmount', and 'InvoiceAmount'
                fig_bar_location.add_trace(go.Scatter(x=location_df['BrLocName'], y=location_df['PaidAmount'],
                                                    mode='lines+markers', name='PaidAmount', line=dict(color='red')))
                fig_bar_location.add_trace(go.Scatter(x=location_df['BrLocName'], y=location_df['BalAmount'],
                                                    mode='lines+markers', name='BalanceAmount', line=dict(color='blue')))
                #fig_bar_location.add_trace(go.Scatter(x=location_df['BrLocName'], y=location_df['InvoiceAmount'],
                                                   #mode='lines+markers', name='InvoiceAmount', line=dict(color='green')))


                st.plotly_chart(fig_bar_location, use_container_width=True)






            with col2:
               
               # Group by 'BrLocName', 'InvType', and calculate the sum for each group
                result_df = df_out.groupby(['BrLocName', 'InvType']).agg(
                    TotalInvoiceAmount=('InvoiceAmount', 'sum'),
                    TotalPaidAmount=('PaidAmount', 'sum'),
                    TotalBalanceAmount=('BalAmount', 'sum')
                ).reset_index()

                # Streamlit app
                st.header('Total Amounts Analysis')

                # Display the DataFrame using st.dataframe
                st.dataframe(result_df, height=450)  # Set the height as needed

            nes1,nes2 = st.columns(2)
            with nes1:
                # Invoice Type Distribution (Pie Chart)
                slice_to_cut = 0
                st.header('Invoice Type Distribution')
                fig_pie_type = px.pie(df_out, names='InvType', title='Invoice Type Distribution', hole=0.3,)  
                fig_pie_type.update_traces(
                    # Show additional information on hover
                    marker=dict(line=dict(color='white', width=2)),  # Add white border for better visibility
                    pull=[0.2 if i == slice_to_cut else 0 for i in range(len(df_out))]
                )
                st.plotly_chart(fig_pie_type, use_container_width=True)

            with nes2:
                st.header('Branches with Arrear and Normal Invoices')
                nest1,nest2 = st.columns(2)
                
                with nest1:
                    # Display all observations in a readable format
                    #st.write("Observations:")
                    # Display branch names and amounts
                    

                    # Branches with Arrear Invoices
                    st.write(f"<b>Branches with Arrear Invoices:</b>", unsafe_allow_html=True)
                    arrear_branches = result_df[result_df['InvType'] == 'Arrear']
                    for branch_name, total_amount in zip(arrear_branches['BrLocName'], arrear_branches['TotalBalanceAmount']):
                        st.write(f"<b>{branch_name}</b>, Total Arrear Balance Amount: <b>{total_amount}</b>", unsafe_allow_html=True)
                with nest2:
                # Branches with Normal Invoices
                    st.write(f"\n<b>Branches with Normal Invoices:</b>", unsafe_allow_html=True)
                    normal_branches = result_df[result_df['InvType'] == 'Normal']
                    for branch_name, total_amount in zip(normal_branches['BrLocName'], normal_branches['TotalBalanceAmount']):
                        st.write(f"<b>{branch_name}</b>, Total Normal Balance Amount: <b>{total_amount}</b>", unsafe_allow_html=True)


    def sideBar(self):
        #pass
        self.option_menu_fun()




if __name__ == "__main__":
    app = DashboardApp()
    #app.main()
    app.sideBar()