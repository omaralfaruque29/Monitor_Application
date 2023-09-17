from flask import Blueprint
import pprint
import json
from flask import Flask
from flask import request,jsonify,abort,render_template,session,redirect,url_for
import collections
import json
from random import randint
import threading
import time
from flask import g

from influxdb import DataFrameClient
import json
import dateutil.parser as parser
import time
import datetime
import os

from app.module_user.controllers import token_auth
from app.process_engine import getFieldList, routeDefaultData, routeTimeIntervalData, routeForecastAlgo, getHostPageCount, getHostList

mod_main = Blueprint('main',__name__,template_folder='templates')

host='10.10.10.84'
port=8086
user = ''
password = ''
dbname = 'telegraf'

#####################################################      Pages     #########################################################################

@mod_main.route('/index', methods = ['GET'])
def index():
	if request.method == 'GET':
		return render_template('index.html'),200,{'Access-Control-Allow-Origin': '*'}
                

@mod_main.route('/loginform', methods = ['GET'])
def login_form():
	if request.method == 'GET':
                return render_template('login.html'),200,{'Access-Control-Allow-Origin': '*'}


@mod_main.route('/stats_by_host/<int:page_no>', methods = ['GET'])
def stats_by_host(page_no):
        if request.method == 'GET':
		offset = (page_no) * 5
                page_count = getHostPageCount()
		host_list  = getHostList(offset)     
                return render_template('stats_by_host.html',host_list=host_list,count=page_count),200,{'Access-Control-Allow-Origin': '*'}



@mod_main.route('/all_graph_by_host/<host_name>', methods = ['GET'])
def all_graph_by_host(host_name):
        if request.method == 'GET':   
		return render_template('all_graph_by_host.html',host_name=host_name),200,{'Access-Control-Allow-Origin': '*'}                                             


@mod_main.route('/detail_graph_by_host/<host_name>/<measurement>', methods = ['GET'])
def detail_graph_by_host(host_name, measurement):
        if request.method == 'GET':
		
		if measurement == 'cpu':
			field_list = getFieldList(host, port, user, password, dbname, measurement)
			return render_template('detail_graph_by_host.html',host_name=host_name, measurement=measurement, field_list=field_list),200,{'Access-Control-Allow-Origin': '*'}

		elif measurement == 'mem':
			field_list = getFieldList(host, port, user, password, dbname, measurement)
			return render_template('detail_graph_by_host.html',host_name=host_name, measurement=measurement, field_list=field_list),200,{'Access-Control-Allow-Origin': '*'} 

		elif measurement == 'net':
			field_list = getFieldList(host, port, user, password, dbname, measurement)
			return render_template('detail_graph_by_host.html',host_name=host_name, measurement=measurement, field_list=field_list),200,{'Access-Control-Allow-Origin': '*'} 

		elif measurement == 'diskio':
			field_list = getFieldList(host, port, user, password, dbname, measurement)
			return render_template('detail_graph_by_host.html',host_name=host_name, measurement=measurement, field_list=field_list),200,{'Access-Control-Allow-Origin': '*'}

		elif measurement == 'disk':
			field_list = getFieldList(host, port, user, password, dbname, measurement)
			return render_template('detail_graph_by_host.html',host_name=host_name, measurement=measurement, field_list=field_list),200,{'Access-Control-Allow-Origin': '*'}

		elif measurement == 'kernel':
			field_list = getFieldList(host, port, user, password, dbname, measurement)
			return render_template('detail_graph_by_host.html',host_name=host_name, measurement=measurement, field_list=field_list),200,{'Access-Control-Allow-Origin': '*'}      

		elif measurement == 'netstat':
			field_list = getFieldList(host, port, user, password, dbname, measurement)
			return render_template('detail_graph_by_host.html',host_name=host_name, measurement=measurement, field_list=field_list),200,{'Access-Control-Allow-Origin': '*'}

		elif measurement == 'processes':
			field_list = getFieldList(host, port, user, password, dbname, measurement)
			return render_template('detail_graph_by_host.html',host_name=host_name, measurement=measurement, field_list=field_list),200,{'Access-Control-Allow-Origin': '*'} 

		elif measurement == 'swap':
			field_list = getFieldList(host, port, user, password, dbname, measurement)
			return render_template('detail_graph_by_host.html',host_name=host_name, measurement=measurement, field_list=field_list),200,{'Access-Control-Allow-Origin': '*'} 

		elif measurement == 'system':
			field_list = getFieldList(host, port, user, password, dbname, measurement)
			return render_template('detail_graph_by_host.html',host_name=host_name, measurement=measurement, field_list=field_list),200,{'Access-Control-Allow-Origin': '*'}  









#############cpu##############
@mod_main.route('/api/v1/cpu_data/<host_name>/<field_name>', methods = ['GET'])
def cpu_data(host_name , field_name):
        if request.method == 'GET':
                return routeDefaultData(host_name, field_name, 'cpu')


@mod_main.route('/api/v1/cpu_data_details/<host_name>/<field_name>/<from_date>/<to_date>', methods = ['GET'])
def cpu_data_details(host_name,field_name,from_date,to_date):
        if request.method == 'GET':
		return routeTimeIntervalData(host_name,field_name,from_date,to_date, 'cpu') 


@mod_main.route('/api/v1/cpu_data_forcast/<algorithm>/<int:number_of_prediction>', methods = ['GET'])
def cpu_data_forcast(algorithm,number_of_prediction):
        if request.method == 'GET':
		return routeForecastAlgo(algorithm, number_of_prediction, 'cpu')


##############disk############
@mod_main.route('/api/v1/disk_data/<host_name>/<field_name>', methods = ['GET'])
def disk_data(host_name, field_name):
        if request.method == 'GET':
		return routeDefaultData(host_name, field_name, 'disk') 

@mod_main.route('/api/v1/disk_data_details/<host_name>/<field_name>/<from_date>/<to_date>', methods = ['GET'])
def disk_data_details(host_name,field_name,from_date,to_date):
        if request.method == 'GET':
                return routeTimeIntervalData(host_name,field_name,from_date,to_date, 'disk')

@mod_main.route('/api/v1/disk_data_forcast/<algorithm>/<int:number_of_prediction>', methods = ['GET'])
def disk_data_forcast(algorithm,number_of_prediction):
        if request.method == 'GET':
                return routeForecastAlgo(algorithm, number_of_prediction, 'disk')


##############diskio############
@mod_main.route('/api/v1/diskio_data/<host_name>/<field_name>', methods = ['GET'])
def diskio_data(host_name, field_name):
        if request.method == 'GET':
		return routeDefaultData(host_name, field_name, 'diskio') 

@mod_main.route('/api/v1/diskio_data_details/<host_name>/<field_name>/<from_date>/<to_date>', methods = ['GET'])
def diskio_data_details(host_name,field_name,from_date,to_date):
        if request.method == 'GET':
                return routeTimeIntervalData(host_name,field_name,from_date,to_date, 'diskio')

@mod_main.route('/api/v1/diskio_data_forcast/<algorithm>/<int:number_of_prediction>', methods = ['GET'])
def diskio_data_forcast(algorithm,number_of_prediction):
        if request.method == 'GET':
                return routeForecastAlgo(algorithm, number_of_prediction, 'diskio')


#############kernel#############
@mod_main.route('/api/v1/kernel_data/<host_name>/<field_name>', methods = ['GET'])
def kernel_data(host_name, field_name):
        if request.method == 'GET':
		return routeDefaultData(host_name, field_name, 'kernel') 

@mod_main.route('/api/v1/kernel_data_details/<host_name>/<field_name>/<from_date>/<to_date>', methods = ['GET'])
def kernel_data_details(host_name,field_name,from_date,to_date):
        if request.method == 'GET':
                return routeTimeIntervalData(host_name,field_name,from_date,to_date, 'kernel')  

@mod_main.route('/api/v1/kernel_data_forcast/<algorithm>/<int:number_of_prediction>', methods = ['GET'])
def kernel_data_forcast(algorithm,number_of_prediction):
        if request.method == 'GET':
                return routeForecastAlgo(algorithm, number_of_prediction, 'kernel') 


############mem#################
@mod_main.route('/api/v1/mem_data/<host_name>/<field_name>', methods = ['GET'])
def mem_data(host_name, field_name):
        if request.method == 'GET':
                return routeDefaultData(host_name, field_name, 'mem') 

@mod_main.route('/api/v1/mem_data_details/<host_name>/<field_name>/<from_date>/<to_date>', methods = ['GET'])
def mem_data_details(host_name,field_name,from_date,to_date):
        if request.method == 'GET':
                return routeTimeIntervalData(host_name,field_name,from_date,to_date, 'mem')     

@mod_main.route('/api/v1/mem_data_forcast/<algorithm>/<int:number_of_prediction>', methods = ['GET'])
def mem_data_forcast(algorithm,number_of_prediction):
        if request.method == 'GET':
                return routeForecastAlgo(algorithm, number_of_prediction, 'mem')


###############net###############
@mod_main.route('/api/v1/net_data/<host_name>/<field_name>', methods = ['GET'])
def net_data(host_name, field_name):
        if request.method == 'GET':
                return routeDefaultData(host_name, field_name, 'net')

@mod_main.route('/api/v1/net_data_details/<host_name>/<field_name>/<from_date>/<to_date>', methods = ['GET'])
def net_data_details(host_name,field_name,from_date,to_date):
        if request.method == 'GET':
                return routeTimeIntervalData(host_name,field_name,from_date,to_date, 'net')  

@mod_main.route('/api/v1/net_data_forcast/<algorithm>/<int:number_of_prediction>', methods = ['GET'])
def net_data_forcast(algorithm,number_of_prediction):
        if request.method == 'GET':
                return routeForecastAlgo(algorithm, number_of_prediction, 'net')  

################netstat############
@mod_main.route('/api/v1/netstat_data/<host_name>/<field_name>', methods = ['GET'])
def netstat_data(host_name, field_name):
        if request.method == 'GET':
		return routeDefaultData(host_name, field_name, 'netstat')

@mod_main.route('/api/v1/netstat_data_details/<host_name>/<field_name>/<from_date>/<to_date>', methods = ['GET'])
def netstat_data_details(host_name,field_name,from_date,to_date):
        if request.method == 'GET':
                return routeTimeIntervalData(host_name,field_name,from_date,to_date, 'netstat') 

@mod_main.route('/api/v1/netstat_data_forcast/<algorithm>/<int:number_of_prediction>', methods = ['GET'])
def netstat_data_forcast(algorithm,number_of_prediction):
        if request.method == 'GET':
                return routeForecastAlgo(algorithm, number_of_prediction, 'netstat') 


##############processes###########
@mod_main.route('/api/v1/processes_data/<host_name>/<field_name>', methods = ['GET'])
def processes_data(host_name, field_name):
        if request.method == 'GET':
		return routeDefaultData(host_name, field_name, 'processes')

@mod_main.route('/api/v1/processes_data_details/<host_name>/<field_name>/<from_date>/<to_date>', methods = ['GET'])
def processes_data_details(host_name,field_name,from_date,to_date):
        if request.method == 'GET':
                return routeTimeIntervalData(host_name,field_name,from_date,to_date, 'processes')  

@mod_main.route('/api/v1/processes_data_forcast/<algorithm>/<int:number_of_prediction>', methods = ['GET'])
def processes_data_forcast(algorithm,number_of_prediction):
        if request.method == 'GET':
                return routeForecastAlgo(algorithm, number_of_prediction, 'processes')   


##############swap###############
@mod_main.route('/api/v1/swap_data/<host_name>/<field_name>', methods = ['GET'])
def swap_data(host_name, field_name):
        if request.method == 'GET':
		return routeDefaultData(host_name, field_name, 'swap')

@mod_main.route('/api/v1/swap_data_details/<host_name>/<field_name>/<from_date>/<to_date>', methods = ['GET'])
def swap_data_details(host_name,field_name,from_date,to_date):
        if request.method == 'GET':
                return routeTimeIntervalData(host_name,field_name,from_date,to_date, 'swap')   

@mod_main.route('/api/v1/swap_data_forcast/<algorithm>/<int:number_of_prediction>', methods = ['GET'])
def swap_data_forcast(algorithm,number_of_prediction):
        if request.method == 'GET':
                return routeForecastAlgo(algorithm, number_of_prediction, 'swap')  


##############system###############
@mod_main.route('/api/v1/system_data/<host_name>/<field_name>', methods = ['GET'])
def system_data(host_name, field_name):
        if request.method == 'GET':
		return routeDefaultData(host_name, field_name, 'system')       

@mod_main.route('/api/v1/system_data_details/<host_name>/<field_name>/<from_date>/<to_date>', methods = ['GET'])
def system_data_details(host_name,field_name,from_date,to_date):
        if request.method == 'GET':
                return routeTimeIntervalData(host_name,field_name,from_date,to_date, 'system')  

@mod_main.route('/api/v1/system_data_forcast/<algorithm>/<int:number_of_prediction>', methods = ['GET'])
def system_data_forcast(algorithm,number_of_prediction):
        if request.method == 'GET':
                return routeForecastAlgo(algorithm, number_of_prediction, 'system')                                                  










                

@mod_main.route('/jvm_stat', methods = ['GET'])
def jvm_stat():
        if request.method == 'GET':
		return render_template('jvm_stat.html'),200,{'Access-Control-Allow-Origin': '*'}      





####################### socket operation ###################################


@mod_main.route('/jvmstat/start/<ip>', methods = ['GET'])
def jvmstat_start(ip):
        if request.method == 'GET':
		start_thread(ip)
		return jsonify({'results':'start'}),200,{'Access-Control-Allow-Origin': '*'}

@mod_main.route('/jvmstat/stop/<ip>', methods = ['GET'])
def jvmstat_stop(ip):
        if request.method == 'GET':
		stop_thread(ip)
		return jsonify({'results':'stop'}),200,{'Access-Control-Allow-Origin': '*'}

@mod_main.route('/jvmstat/refresh/<ip>', methods = ['GET'])
def jvmstat_refresh(ip):
        if request.method == 'GET':
		refresh_thread(ip)
		return jsonify({'results':'refresh'}),200,{'Access-Control-Allow-Origin': '*'}               

@mod_main.route('/jvmstat/thread_id/<ip>/<thread_id>', methods = ['GET'])
def jvmstat_thread_id(ip,thread_id):
        if request.method == 'GET':
		thread_id_thread(ip,thread_id)
		return jsonify({'results':'stop'}),200,{'Access-Control-Allow-Origin': '*'}                                                             




